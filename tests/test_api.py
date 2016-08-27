# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException


def test_invalid_network_id(api):
    old_token = api.network_token
    try:
        api.network_token = 'invalid'
        with pytest.raises(HasOffersException):
            api._call('test', 'test')
    finally:
        api.network_token = old_token


def test_handle_response(api):
    assert api.handle_response({'response': {'data': {'unknown': ''}}}) is None
