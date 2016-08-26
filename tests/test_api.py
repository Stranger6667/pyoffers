# coding: utf-8
import pytest

from pyoffers.exceptions import NetworkIDError


def test_invalid_network_id(api):
    old_token = api.network_token
    try:
        api.network_token = 'invalid'
        with pytest.raises(NetworkIDError):
            api._call('test', 'test')
    finally:
        api.network_token = old_token
