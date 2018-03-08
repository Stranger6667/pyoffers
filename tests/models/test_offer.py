# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Advertiser, Conversion, Country, Offer, OfferCategory


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


def test_get_categories(offer):
    categories = offer.get_categories()
    assert len(categories) == 1
    assert isinstance(categories[0], OfferCategory)


def test_update_category(offer):
    assert offer.get_categories()[0].update(status='deleted') is True


def test_add_category_fail(offer):
    with pytest.raises(HasOffersException) as exc:
        offer.add_category(-1)
    assert str(exc.value) == 'Row id is negative'


def test_block_affiliate_success(offer):
    assert offer.block_affiliate(1) is True


def test_block_affiliate_fail(offer):
    with pytest.raises(HasOffersException) as exc:
        offer.block_affiliate(21)
    assert str(exc.value) == 'Failed to hydrate rows: 21'


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

    def test_find_by_id_array_related(self, api):
        offer = api.offers.find_by_id(438, contain=['Country'])
        assert isinstance(offer, Offer)
        assert isinstance(offer.country, list)
        assert isinstance(offer.country[0], Country)

    def test_find_by_id_single_instance(self, api):
        offer = api.offers.find_by_id(438, contain=['Advertiser'])
        assert isinstance(offer.advertiser, Advertiser)


def test_find_all_ids(api):
    results = api.offers.find_all_ids()
    assert isinstance(results, list)
    assert all(result.isdigit() for result in results)


def test_conversions_manager(offer):
    conversions = offer.conversions.find_all()
    assert len(conversions) == 1
    assert isinstance(conversions[0], Conversion)
    assert conversions[0].offer_id == offer.id
