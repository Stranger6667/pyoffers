# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models import Advertiser

CASSETTE_NAME = "advertiser"


def test_create_success(advertiser):
    assert isinstance(advertiser, Advertiser)
    assert advertiser.country == "CZ"


def test_find_by_id_success(api, advertiser):
    instance = api.advertisers.find_by_id(advertiser.id)
    assert isinstance(instance, Advertiser)
    assert instance.country == "CZ"


def test_find_by_id_fail(api):
    assert api.advertisers.find_by_id(100000) is None


def test_find_all(api):
    result = api.advertisers.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Advertiser) for item in result)


def test_update_success(advertiser):
    new_instance = advertiser.update(company="Another")
    assert new_instance.company == "Another"
    assert new_instance == advertiser


def test_update_fail(advertiser):
    with pytest.raises(HasOffersException) as exc:
        advertiser.update(account_manager_id="string")
    assert str(exc.value) == "Error code: 3. Could not update advertiser. Account_manager_id is not valid."


def test_block_success(advertiser):
    assert advertiser.block("reason text") is True
