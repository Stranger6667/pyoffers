# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Country, Offer


CASSETTE_NAME = 'offer'


def test_create_success(offer):
    assert isinstance(offer, Offer)
    assert offer.offer_url == 'http://www.example.com'


def test_find_by_id_success(api, offer):
    instance = api.offers.find_by_id(offer.id)
    assert isinstance(instance, Offer)
    assert instance.offer_url == offer.offer_url


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
    new_instance = offer.update(offer_url='test.com')
    assert new_instance.offer_url == 'http://test.com'
    assert new_instance == offer


def test_add_target_country_success(offer):
    assert offer.add_target_country('ES') is True


def test_add_category_success(offer):
    assert offer.add_category(1) is True


def test_add_category_fail(offer):
    with pytest.raises(HasOffersException):
        offer.add_category(-1)


class TestContain:

    def test_find_all(self, api):
        offer = api.offers.find_all(id=62, contain=['Country'])[0]
        assert isinstance(offer, Offer)
        assert offer.country.id == '724'

    def test_find_all_empty_related(self, api):
        offers = api.offers.find_all(currency='CZK', contain=['Country'])
        assert offers[0].country is None
        assert offers[1].country.id == '203'

    def test_find_by_id(self, api):
        offer = api.offers.find_by_id(id=62, contain=['Country'])
        assert isinstance(offer, Offer)
        assert offer.country.id == '724'


def test_find_all_ids(api):
    results = api.offers.find_all_ids()
    assert isinstance(results, list)
    assert all(result.isdigit() for result in results)
