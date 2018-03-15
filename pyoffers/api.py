# coding: utf-8
import time
from collections import OrderedDict

import requests

from .exceptions import HasOffersException, MaxRetriesExceeded
from .logging import get_logger
from .models import MANAGER_ALIASES, MODEL_MANAGERS, ApplicationManager
from .utils import prepare_query_params


def is_empty(data):
    return isinstance(data, bool) or not data


def is_paginated(data):
    return 'pageCount' in data


def retry(method):
    """
    Allows to retry method execution few times.
    """

    def inner(self, *args, **kwargs):
        attempt_number = 1
        while attempt_number < self.retries:
            try:
                return method(self, *args, **kwargs)
            except HasOffersException as exc:
                if 'API usage exceeded rate limit' not in str(exc):
                    raise exc
                self.logger.debug('Retrying due: %s', exc)
                time.sleep(self.retry_timeout)
            except requests.exceptions.ConnectionError:
                # This happens when the session gets expired
                self.logger.debug('Recreating session due to ConnectionError')
                self._session = requests.Session()
            attempt_number += 1
        raise MaxRetriesExceeded

    return inner


class HasOffersAPI:
    """
    Client to communicate with HasOffers API.
    """

    def __init__(self, endpoint=None, network_token=None, network_id=None, verify=True, retries=3, retry_timeout=3,
                 verbosity=0):
        self.endpoint = endpoint
        self.network_token = network_token
        self.network_id = network_id
        self.verify = verify
        self.retries = retries
        self.retry_timeout = retry_timeout
        self.logger = get_logger(verbosity)
        self._session = None
        self.setup_managers()

    def setup_managers(self):
        """
        Allows to access manager by model name - it is convenient, because HasOffers returns model names in responses.
        """
        self._managers = {}
        for manager_class in MODEL_MANAGERS:
            instance = manager_class(self)
            if not isinstance(instance, ApplicationManager) or instance.__class__ is ApplicationManager:
                # Descendants of ``ApplicationManager`` shouldn't be present in API instance.  They are controlled by
                # Application controller. The manager itself, on the other hand, should.
                setattr(self, instance.name, instance)
            if instance.model:
                self._managers[instance.model.__name__] = instance

    def __str__(self):
        return '%s: %s / %s' % (self.__class__.__name__, self.network_token, self.network_id)

    def __repr__(self):
        return '<%s>' % self

    @property
    def session(self):
        if not self._session:
            self._session = requests.Session()
        return self._session

    @retry
    def _call(self, target, method, single_result=True, raw=False, files=None, **kwargs):
        """
        Low-level call to HasOffers API.
        """
        params = prepare_query_params(
            NetworkToken=self.network_token,
            NetworkId=self.network_id,
            Target=target,
            Method=method,
            **kwargs
        )
        kwargs = {'url': self.endpoint, 'params': params, 'verify': self.verify, 'method': 'GET'}
        if files:
            kwargs.update({'method': 'POST', 'files': files})

        self.logger.debug('Request parameters: %s', params)
        response = self.session.request(**kwargs)

        self.logger.debug('Response [%s]: %s', response.status_code, response.text)
        response.raise_for_status()
        data = response.json(object_pairs_hook=OrderedDict)
        return self.handle_response(data, target=target, single_result=single_result, raw=raw)

    def handle_response(self, content, target=None, single_result=True, raw=False):
        """
        Parses response, checks it.
        """
        response = content['response']

        self.check_errors(response)

        data = response.get('data')

        if is_empty(data):
            return data
        elif is_paginated(data):
            if not data['count']:
                return data['data']
            data = data['data']

        if raw:
            return data
        return self.init_all_objects(data, target=target, single_result=single_result)

    def check_errors(self, response):
        errors = response.get('errors')
        if errors:
            raise HasOffersException(errors)

    def init_all_objects(self, data, target=None, single_result=True):
        """
        Initializes model instances from given data.
        Returns single instance if single_result=True.
        """
        if single_result:
            return self.init_target_object(target, data)
        return list(self.expand_models(target, data))

    def init_target_object(self, target, data):
        """
        Initializes target object and assign extra objects to target as attributes
        """
        target_object = self.init_single_object(target, data.pop(target))
        for key, item in data.items():
            key_alias = MANAGER_ALIASES.get(key, key)
            if item:
                # Item is an OrderedDict with 3 possible structure patterns:
                #   - Just an OrderedDict with (key - value)'s
                #   - OrderedDict with single (key - OrderedDict)
                #   - OrderedDict with multiple (key - OrderedDict)'s
                first_key = list(item.keys())[0]
                if isinstance(item[first_key], OrderedDict):
                    instances = item.values()
                    if len(instances) > 1:
                        children = [self.init_single_object(key_alias, instance) for instance in instances]
                    else:
                        children = self.init_single_object(key_alias, list(instances)[0])
                else:
                    children = self.init_single_object(key_alias, item)
                setattr(target_object, key.lower(), children)
            else:
                setattr(target_object, key.lower(), None)
        return target_object

    def init_single_object(self, target, data):
        if data:
            return self._managers[target].init_instance(data)

    def expand_models(self, target, data):
        """
        Generates all objects from given data.
        """
        if isinstance(data, dict):
            data = data.values()
        for chunk in data:
            if target in chunk:
                yield self.init_target_object(target, chunk)
            else:
                for key, item in chunk.items():
                    yield self.init_single_object(key, item)
