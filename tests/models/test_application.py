# coding: utf-8
from pyoffers.models import OfferCategory


CASSETTE_NAME = 'application'


def test_find_all_offer_categories(api):
    result = api.application.find_all_offer_categories()
    assert isinstance(result, list)
    assert isinstance(result[0], OfferCategory)


def test_find_all_offer_category_offer_ids(api):
    result = api.application.find_all_offer_category_offer_ids(10)
    assert len(result) == 1
