# coding: utf-8
import requests

from .exceptions import HasOffersException
from .logging import get_logger
from .models import AdvertiserManager, ConversionManager, GoalManager, ModelManager, OfferManager
from .utils import prepare_query_params


class APIMeta(type):
    """
    Adds managers cache to API class.
    Allows to access manager by model name - it is convenient, because HasOffers returns model names in responses.
    """

    def __new__(mcs, name, bases, members):
        members['_managers'] = {
            member.model.__name__: member
            for name, member in members.items()
            if isinstance(member, ModelManager)
        }
        return super().__new__(mcs, name, bases, members)


def is_empty(data):
    return isinstance(data, bool) or not data


def is_paginated(data):
    return 'pageCount' in data


def is_multiple_objects(data):
    return len(data) > 1


class HasOffersAPI(metaclass=APIMeta):
    """
    Client to communicate with HasOffers API.
    """
    _managers = None
    advertisers = AdvertiserManager()
    conversions = ConversionManager()
    goals = GoalManager()
    offers = OfferManager()

    def __init__(self, endpoint=None, network_token=None, network_id=None, verbosity=0):
        self.endpoint = endpoint
        self.network_token = network_token
        self.network_id = network_id
        self.logger = get_logger(verbosity)
        self.bind_managers()

    def bind_managers(self):
        """
        Binds API instance to manager instance.
        """
        for manager in self._managers.values():
            manager.bind(self)

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
        content = response.json()
        return self.handle_response(content, single_result=single_result)

    def handle_response(self, content, single_result=True):
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
            data = data['data'].values()
        elif is_multiple_objects(data) or not single_result:
            data = data.values()

        return self.init_objects(data, single_result=single_result)

    def check_errors(self, response):
        errors = response.get('errors')
        if errors:
            raise HasOffersException(errors)

    def init_objects(self, data, single_result=True):
        """
        Initializes model instances from given data.
        Returns single instance if single_result=True.
        """
        if single_result:
            key, value = list(data.items())[0]
            return self._managers[key].init_instance(value)
        return [
            self._managers[key].init_instance(item)
            for chunk in data
            for key, item in chunk.items()
        ]
