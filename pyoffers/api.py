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

    def _call(self, target, method, **kwargs):
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
        response.raise_for_status()
        content = response.json()
        self.logger.debug('Response: %s', content)
        return self.handle_response(content)

    def handle_response(self, content):
        """
        Parses response, checks it.
        """
        response = content['response']

        errors = response.get('errors')
        if errors:
            raise HasOffersException(errors)

        data = response.get('data')

        if isinstance(data, bool) or data is None:
            return data
        if 'pageCount' in data:
            if not data['count']:
                return data['data']
            return self.init_objects(*data['data'].values())
        return self.init_objects(data, single=True)

    def init_objects(self, *data, single=False):
        """
        Initializes model instances from given data.
        Returns single instance if it is possible and single=False.
        """
        initialized = [
            self._managers[key].init_instance(item)
            for chunk in data
            for key, item in chunk.items()
        ]
        if len(initialized) == 1 and single:
            return initialized[0]
        return initialized
