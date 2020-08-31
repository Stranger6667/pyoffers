import pytest

from pyoffers.models import Tag
from pyoffers.models.tags import TagRelation

CASSETTE_NAME = "tag"


def test_create_success(tag):
    assert isinstance(tag, Tag)


def test_find_by_id_success(api, tag):
    instance = api.tags.find_by_id(tag.id)
    assert isinstance(instance, Tag)


def test_find_by_id_fail(api):
    assert api.offers.find_by_id(1000) is None


def test_find_all(api):
    result = api.tags.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Tag) for item in result)


def test_add_to_offer(tag, offer):
    assert isinstance(tag.add_to_offer(offer.id), TagRelation)


def test_add_to_affiliate(tag, affiliate):
    assert isinstance(tag.add_to_affiliate(affiliate.id), TagRelation)


def test_add_to_advertiser(tag, advertiser):
    assert isinstance(tag.add_to_advertiser(advertiser.id), TagRelation)


def test_set_for_offer(api, offer):
    assert api.tags.set_for_offer([286, 288], offer.id)


def test_set_for_affiliate(api, affiliate):
    assert api.tags.set_for_affiliate([286, 288], affiliate.id)


def test_set_for_advertiser(api, advertiser):
    assert api.tags.set_for_advertiser([286, 288], advertiser.id)


def test_remove_from_offer(tag, offer):
    assert isinstance(tag.remove_from_offer(offer.id), int)


def test_remove_from_affiliate(tag, affiliate):
    assert isinstance(tag.remove_from_affiliate(affiliate.id), int)


def test_remove_from_advertiser(tag, advertiser):
    assert isinstance(tag.remove_from_advertiser(advertiser.id), int)


def test_find_all_offer_tag_relations(api):
    assert isinstance(api.tags.find_all_offer_tag_relations(), list)


def test_find_all_affiliate_tag_relations(api):
    assert isinstance(api.tags.find_all_affiliate_tag_relations(), list)


def test_find_all_advertiser_tag_relations(api):
    assert isinstance(api.tags.find_all_advertiser_tag_relations(), list)


def test_remove_from_advertiser_by_relational_id(api):
    assert api.tags.remove_from_advertiser_by_relational_id(8)


@pytest.mark.skip(reason="Method does not work in HO")
def test_remove_from_offer_by_relational_id(api):
    assert api.tags.remove_from_offer_by_relational_id(196)


@pytest.mark.skip(reason="Method does not work in HO")
def test_remove_from_affiliate_by_relational_id(api):
    assert api.tags.remove_from_affiliate_by_relational_id(82)
