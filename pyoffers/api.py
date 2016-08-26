# coding: utf-8
import requests

from .exceptions import check_errors
from .logging import get_logger
from .models.advertiser import Advertiser, AdvertiserManager
from .models.offer import Offer, OfferManager
from .utils import add_get_args


class HasOffersAPI:
    managers = {
        'advertisers': AdvertiserManager,
        'offers': OfferManager
    }

    def __init__(self, endpoint=None, network_token=None, network_id=None, verbosity=0):
        self.endpoint = endpoint
        self.network_token = network_token
        self.network_id = network_id
        self.logger = get_logger(verbosity)
        for name, manager in self.managers.items():
            setattr(self, name, manager(self))

    def _call(self, target, method, **kwargs):
        """
        Low-level call to HasOffers API.
        """
        params = {
            'NetworkToken': self.network_token,
            'NetworkId': self.network_id,
            'Target': target,
            'Method': method
        }
        params.update(**kwargs)
        url = add_get_args(self.endpoint, **params)
        response = requests.get(url, verify=False)
        response.raise_for_status()
        content = response.json()
        self.logger.debug('Response: %s', content)
        return self.handle_response(content)

    def handle_response(self, content):
        """
        Parses response, checks it.
        """
        response = content['response']

        check_errors(response.get('errors'))

        data = response.get('data')

        if isinstance(data, bool) or data is None:
            return data
        elif isinstance(data, dict):
            if 'Advertiser' in data:
                return Advertiser(manager=self.advertisers, **data['Advertiser'])
            elif 'Offer' in data:
                return Offer(manager=self.offers, **data['Offer'])
        return content
