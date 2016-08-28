# coding: utf-8
import requests

from .exceptions import HasOffersException
from .logging import get_logger
from .models.advertiser import Advertiser, AdvertiserManager
from .models.goal import Goal, GoalManager
from .models.offer import Offer, OfferManager
from .utils import prepare_query_params


class HasOffersAPI:
    """
    Client to communicate with HasOffers API.
    """
    managers = {
        'advertisers': AdvertiserManager,
        'goals': GoalManager,
        'offers': OfferManager,
    }

    def __init__(self, endpoint=None, network_token=None, network_id=None, verbosity=0):
        self.endpoint = endpoint
        self.network_token = network_token
        self.network_id = network_id
        self.logger = get_logger(verbosity)
        for name, manager in self.managers.items():
            setattr(self, name, manager(self))

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
        if 'Advertiser' in data:
            return Advertiser(manager=self.advertisers, **data['Advertiser'])
        elif 'Offer' in data:
            return Offer(manager=self.offers, **data['Offer'])
        elif 'Goal' in data:
            return Goal(manager=self.goals, **data['Goal'])
