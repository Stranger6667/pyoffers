# coding: utf-8
import requests

from .exceptions import InvalidPathError
from .logging import get_logger
from .models.advertiser import Advertiser, AdvertiserManager
from .utils import add_get_args


class HasOffersAPI:
    managers = {
        'advertisers': AdvertiserManager
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
        data = content['response']
        if data['errors']:
            if data['errors']['publicMessage'] == 'Invalid path for URL':
                raise InvalidPathError
        elif isinstance(data['data'], bool):
            return data['data']
        elif isinstance(data['data'], dict):
            if 'Advertiser' in data['data']:
                return Advertiser(manager=self.advertisers, **data['data']['Advertiser'])
        return data
