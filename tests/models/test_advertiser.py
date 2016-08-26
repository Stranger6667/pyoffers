# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Advertiser


CASSETTE_NAME = 'advertiser'


def test_create_success(advertiser):
    assert isinstance(advertiser, Advertiser)
    assert advertiser['country'] == 'CZ'


def test_get_by_id_success(api, advertiser):
    instance = api.advertisers.find_by_id(advertiser['id'])
    assert isinstance(instance, Advertiser)
    assert instance['country'] == 'CZ'


def test_get_by_id_fail(api):
    assert api.advertisers.find_by_id(100000) is None


def test_update_success(advertiser):
    advertiser['company'] = 'Another'
    new_instance = advertiser.update()
    assert new_instance['company'] == 'Another'
    assert new_instance == advertiser


def test_update_fail(advertiser):
    advertiser['account_manager_id'] = 'string'
    with pytest.raises(HasOffersException):
        advertiser.update()


def test_block_success(advertiser):
    assert advertiser.block('reason text') is True
