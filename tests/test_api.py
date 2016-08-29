# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Advertiser


def test_invalid_network_id(api):
    old_token = api.network_token
    try:
        api.network_token = 'invalid'
        with pytest.raises(HasOffersException):
            api._call('test', 'test')
    finally:
        api.network_token = old_token


class TestHandleResponse:

    def test_unknown_response(self, api):
        assert api.handle_response({'response': {'data': {'unknown': ''}}}) is None

    def test_multiple_objects(self, api):
        data = {
            'response': {
                'errors': [],
                'data': {
                    'pageCount': 12,
                    'page': 1,
                    'data': {
                        '114': {'Advertiser': {'country': 'CZ', 'id': '114'}},
                        '108': {'Advertiser': {'country': 'PL', 'id': '108'}},
                    },
                    'current': 0,
                    'count': 59
                },
                'httpStatus': 200,
                'status': 1,
                'errorMessage': None
            },
        }
        cz_adv, pl_adv = sorted(api.handle_response(data), key=lambda x: x['country'])
        assert isinstance(cz_adv, Advertiser)
        assert cz_adv['id'] == '114'
        assert cz_adv['country'] == 'CZ'
        assert isinstance(pl_adv, Advertiser)
        assert pl_adv['id'] == '108'
        assert pl_adv['country'] == 'PL'


def test_str(api):
    assert str(api) == 'HasOffersAPI: token / id'


def test_repr(api):
    assert repr(api) == '<HasOffersAPI: token / id>'
