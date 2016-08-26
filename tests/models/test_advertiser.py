# coding: utf-8
import pytest

from pyoffers.models import Advertiser

from .responses import BLOCK_ADVERTISER_SUCCESS, CREATE_ADVERTISER_SUCCESS, UPDATE_ADVERTISER_SUCCESS


@pytest.mark.response(CREATE_ADVERTISER_SUCCESS)
def test_create_success(api):
    instance = api.advertisers.create(status='pending', company='Test', country='CZ', zipcode='123456')
    assert isinstance(instance, Advertiser)
    assert instance['country'] == 'CZ'


@pytest.mark.response(UPDATE_ADVERTISER_SUCCESS)
def test_update_success(advertiser):
    advertiser['company'] = 'Another'
    new_instance = advertiser.save()
    assert new_instance['company'] == 'Another'
    assert new_instance == advertiser


@pytest.mark.response(BLOCK_ADVERTISER_SUCCESS)
def test_block_success(advertiser):
    assert advertiser.block('reason text') is True
