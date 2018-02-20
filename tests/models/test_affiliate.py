# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Affiliate, AffiliateUser


CASSETTE_NAME = 'affiliate'


def test_create_success(affiliate_with_user):
    assert isinstance(affiliate_with_user, Affiliate)
    assert affiliate_with_user.country == 'USA'
    assert isinstance(affiliate_with_user.user, AffiliateUser)


def test_create_without_user(affiliate):
    assert isinstance(affiliate, Affiliate)
    assert affiliate.user is None


def test_find_by_id_success(api, affiliate_with_user):
    instance = api.affiliates.find_by_id(affiliate_with_user.id)
    assert isinstance(instance, Affiliate)
    assert instance.company == affiliate_with_user.company


def test_find_by_id_failure(api):
    assert api.affiliates.find_by_id(43) is None


def test_find_all(api):
    result = api.affiliates.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Affiliate) for item in result)


def test_update_success(affiliate_with_user):
    new_instance = affiliate_with_user.update(company='New Company')
    assert new_instance.company == 'New Company'


def test_update_fail(affiliate_with_user):
    with pytest.raises(HasOffersException) as exc:
        affiliate_with_user.update(status='null')
        assert str(exc.value) == 'Error code: 3. Could not update affiliate. Status must be one of: ' \
                                 'pending, active, blocked, deleted, rejected'


def test_block(affiliate):
    assert affiliate.block(reason='why') is True


def test_delete(affiliate_with_user, api):
    affiliate_with_user.delete()
    assert api.affiliates.find_by_id(affiliate_with_user.id).status == 'deleted'
