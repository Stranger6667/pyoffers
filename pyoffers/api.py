# coding: utf-8
from collections import OrderedDict

import requests

from .exceptions import HasOffersException
from .logging import get_logger
from .models import MODEL_MANAGERS
from .utils import prepare_query_params


def is_empty(data):
    return isinstance(data, bool) or not data


def is_paginated(data):
    return 'pageCount' in data


class HasOffersAPI:
    """
    Client to communicate with HasOffers API.
    """

    def __init__(self, endpoint=None, network_token=None, network_id=None, verbosity=0):
        self.endpoint = endpoint
        self.network_token = network_token
        self.network_id = network_id
        self.logger = get_logger(verbosity)
        self.setup_managers()

    def setup_managers(self):
        """
        Allows to access manager by model name - it is convenient, because HasOffers returns model names in responses.
        """
        self._managers = {}
        for manager_class in MODEL_MANAGERS:
            instance = manager_class(self)
            setattr(self, instance.name, instance)
            self._managers[instance.model.__name__] = instance

    def __str__(self):
        return '%s: %s / %s' % (self.__class__.__name__, self.network_token, self.network_id)

    def __repr__(self):
        return '<%s>' % self

    @property
    def session(self):
        if not hasattr(self, '_session'):
            self._session = requests.Session()
        return self._session

    def _call(self, target, method, single_result=True, **kwargs):
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
        response = self.session.get(self.endpoint, params=params, verify=False)
        self.logger.debug('Request parameters: %s', params)
        self.logger.debug('Response [%s]: %s', response.status_code, response.text)
        response.raise_for_status()
        data = response.json(object_pairs_hook=OrderedDict)
        return self.handle_response(data, target=target, single_result=single_result)

    def handle_response(self, content, target=None, single_result=True):
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
            setattr(target_object, key.lower(), self.init_single_object(key, item))
        return target_object

    def init_single_object(self, target, data):
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
