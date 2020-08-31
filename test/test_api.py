from unittest.mock import patch

import pytest
import requests

from pyoffers.api import HasOffersAPI
from pyoffers.exceptions import HasOffersException, MaxRetriesExceeded
from pyoffers.models import Advertiser, Country


def test_invalid_network_id(api):
    old_token = api.network_token
    try:
        api.network_token = "invalid"
        with pytest.raises(HasOffersException) as exc:
            api._call("test", "test")
        assert str(exc.value) == "Network id is not valid"
    finally:
        api.network_token = old_token


class TestHandleResponse:
    def test_multiple_objects(self, api):
        data = {
            "response": {
                "errors": [],
                "data": {
                    "pageCount": 12,
                    "page": 1,
                    "data": {
                        "114": {"Advertiser": {"country": "CZ", "id": "114"}},
                        "108": {"Advertiser": {"country": "PL", "id": "108"}},
                    },
                    "current": 0,
                    "count": 59,
                },
                "httpStatus": 200,
                "status": 1,
                "errorMessage": None,
            },
        }
        cz_adv, pl_adv = sorted(
            api.handle_response(data, target="Advertiser", single_result=False), key=lambda x: x.country
        )
        assert isinstance(cz_adv, Advertiser)
        assert cz_adv.id == "114"
        assert cz_adv.country == "CZ"
        assert isinstance(pl_adv, Advertiser)
        assert pl_adv.id == "108"
        assert pl_adv.country == "PL"


def test_str(api):
    assert str(api) == "HasOffersAPI: token / id"


def test_repr(api):
    assert repr(api) == "<HasOffersAPI: token / id>"


def test_multiple_api_instances():
    first = HasOffersAPI()
    second = HasOffersAPI()
    assert all(manager.api is first for manager in first._managers.values())
    assert all(manager.api is second for manager in second._managers.values())


class TestGenericMethod:
    def test_manager(self, api):
        assert not hasattr(api.countries, "create")

    def test_model(self):
        assert not hasattr(Country({}), "update")


def test_raw(api):
    assert isinstance(api.advertisers._call("findAllIds", raw=True), list)


def test_session_recreation(api):
    session = api.session
    with pytest.raises(MaxRetriesExceeded), patch(
        "requests.sessions.Session.request", side_effect=requests.exceptions.ConnectionError
    ) as get:
        isinstance(api.advertisers._call("findAllIds", raw=True), list)
        assert get.call_count == 3
        assert api.session is not session
