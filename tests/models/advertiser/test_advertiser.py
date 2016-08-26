# coding: utf-8
import pytest

from pyoffers.exceptions import InputError
from pyoffers.models import Advertiser

from .responses import (
    BLOCK_ADVERTISER_SUCCESS,
    CREATE_ADVERTISER_SUCCESS,
    FIND_BY_ID_ADVERTISER_FAIL,
    FIND_BY_ID_ADVERTISER_SUCCESS,
    UPDATE_ADVERTISER_FAIL,
    UPDATE_ADVERTISER_SUCCESS,
)


@pytest.mark.response(CREATE_ADVERTISER_SUCCESS)
def test_create_success(api):
    instance = api.advertisers.create(status='pending', company='Test', country='CZ', zipcode='123456')
    assert isinstance(instance, Advertiser)
    assert instance['country'] == 'CZ'


@pytest.mark.response(FIND_BY_ID_ADVERTISER_SUCCESS)
def test_get_by_id_success(api):
    instance = api.advertisers.find_by_id(1)
    assert isinstance(instance, Advertiser)
    assert instance['country'] == 'CZ'


@pytest.mark.response(FIND_BY_ID_ADVERTISER_FAIL)
def test_get_by_id_fail(api):
    assert api.advertisers.find_by_id(1000) is None


@pytest.mark.response(UPDATE_ADVERTISER_SUCCESS)
def test_update_success(advertiser):
    advertiser['company'] = 'Another'
    new_instance = advertiser.update()
    assert new_instance['company'] == 'Another'
    assert new_instance == advertiser


@pytest.mark.response(UPDATE_ADVERTISER_FAIL)
def test_update_fail(advertiser):
    advertiser['company'] = 123
    with pytest.raises(InputError):
        advertiser.update()


@pytest.mark.response(BLOCK_ADVERTISER_SUCCESS)
def test_block_success(advertiser):
    assert advertiser.block('reason text') is True
