# coding: utf-8
import pytest

from pyoffers.exceptions import InputError
from pyoffers.models import Offer

from .responses import (
    ADD_CATEGORY_FAIL,
    ADD_CATEGORY_SUCCESS,
    ADD_TARGET_COUNTRY_SUCCESS,
    CREATE_OFFER_FAIL,
    CREATE_OFFER_SUCCESS,
    FIND_BY_ID_OFFER_FAIL,
    FIND_BY_ID_OFFER_SUCCESS,
    UPDATE_OFFER_SUCCESS,
)


URL = 'http://example.com'


@pytest.mark.response(CREATE_OFFER_FAIL)
def test_create_fail(api):
    with pytest.raises(InputError):
        api.offers.create(status='pending')


@pytest.mark.response(CREATE_OFFER_SUCCESS)
def test_create_success(api):
    instance = api.offers.create(
        name='Test', offer_url=URL, status='pending', expiration_date='2030-12-12 23:59:59', preview_url=URL
    )
    assert isinstance(instance, Offer)
    assert instance['offer_url'] == URL


@pytest.mark.response(FIND_BY_ID_OFFER_SUCCESS)
def test_get_by_id_success(api):
    instance = api.offers.find_by_id(1)
    assert isinstance(instance, Offer)
    assert instance['offer_url'] == URL


@pytest.mark.response(FIND_BY_ID_OFFER_FAIL)
def test_get_by_id_fail(api):
    assert api.offers.find_by_id(1000) is None


@pytest.mark.response(UPDATE_OFFER_SUCCESS)
def test_update_success(offer):
    offer['offer_url'] = 'test.com'
    new_instance = offer.update()
    assert new_instance['offer_url'] == 'http://test.com'
    assert new_instance == offer


@pytest.mark.response(ADD_TARGET_COUNTRY_SUCCESS)
def test_add_target_country_success(offer):
    assert offer.add_target_country('ES') is True


@pytest.mark.response(ADD_CATEGORY_SUCCESS)
def test_add_category_success(offer):
    assert offer.add_category(1) is True


@pytest.mark.response(ADD_CATEGORY_FAIL)
def test_add_category_fail(offer):
    with pytest.raises(InputError):
        offer.add_category(-1)
