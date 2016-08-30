# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Country, Offer


CASSETTE_NAME = 'offer'


def test_create_success(offer):
    assert isinstance(offer, Offer)
    assert offer['offer_url'] == 'http://www.example.com'


def test_find_by_id_success(api, offer):
    instance = api.offers.find_by_id(offer['id'])
    assert isinstance(instance, Offer)
    assert instance['offer_url'] == offer['offer_url']


def test_find_by_id_fail(api):
    assert api.offers.find_by_id(1000) is None


def test_find_all(api):
    result = api.offers.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Offer) for item in result)


def test_get_target_countries(api):
    result = api.offers.get_target_countries(id=46)
    assert len(result) == 1
    assert all(isinstance(item, Country) for item in result)


def test_get_target_countries_empty(offer):
    assert offer.get_target_countries() == []


def test_update_success(offer):
    offer['offer_url'] = 'test.com'
    new_instance = offer.update()
    assert new_instance['offer_url'] == 'http://test.com'
    assert new_instance == offer


def test_add_target_country_success(offer):
    assert offer.add_target_country('ES') is True


def test_add_category_success(offer):
    assert offer.add_category(1) is True


def test_add_category_fail(offer):
    with pytest.raises(HasOffersException):
        offer.add_category(-1)
