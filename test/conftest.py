# coding: utf-8
import os

import pytest
from betamax import Betamax
from betamax_serializers import pretty_json

from pyoffers.api import HasOffersAPI

from .helpers import replace_real_credentials

Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

URL = "http://www.example.com"
CASSETTE_DIR = "test/cassettes/"
DEFAULT_NETWORK_TOKEN = "token"
DEFAULT_NETWORK_ID = "id"
NETWORK_TOKEN = os.environ.get("NETWORK_TOKEN", DEFAULT_NETWORK_TOKEN)
NETWORK_ID = os.environ.get("NETWORK_ID", DEFAULT_NETWORK_ID)


def pytest_addoption(parser):
    parser.addoption("--record", action="store_true", help="Runs cleanup for recording session")


def pytest_unconfigure(config):
    if config.getoption("--record"):
        replace_real_credentials(CASSETTE_DIR, NETWORK_TOKEN, DEFAULT_NETWORK_TOKEN, NETWORK_ID, DEFAULT_NETWORK_ID)


@pytest.fixture(autouse=True, scope="module")
def betamax_recorder(request, api):
    """Module level Betamax recorder."""
    if request.config.getoption("--record"):
        record_mode = "new_episodes"
    else:
        record_mode = "none"
    cassette_name = getattr(request.node._obj, "CASSETTE_NAME", "default")
    vcr = Betamax(
        api.session,
        cassette_library_dir=CASSETTE_DIR,
        default_cassette_options={
            "preserve_exact_body_bytes": True,
            "serialize_with": "prettyjson",
            "match_requests_on": ["query", "method"],
            "record_mode": record_mode,
        },
    )
    with vcr.use_cassette(cassette_name):
        yield


@pytest.fixture(scope="module")
def api():
    return HasOffersAPI(
        endpoint="https://api.hasoffers.com/Apiv3/json", network_token=NETWORK_TOKEN, network_id=NETWORK_ID
    )


@pytest.fixture(scope="module")
def advertiser(api):
    return api.advertisers.create(status="pending", company="Test", country="CZ", zipcode="123456")


@pytest.fixture(scope="module")
def offer(api):
    return api.offers.create(
        name="Test", offer_url=URL, status="pending", expiration_date="2030-12-12 23:59:59", preview_url=URL
    )


@pytest.fixture(scope="module")
def conversion(api):
    return api.conversions.create(
        status="pending", payout="1", revenue="1", affiliate_id="1", offer_id="1", status_code="22"
    )


@pytest.fixture(scope="module")
def goal(api, offer):
    return api.goals.create(name="Test", description="String", status="deleted", offer_id=offer.id)


@pytest.fixture(scope="module")
def date_dirs(api):
    return api.raw_logs.clicks.list_date_dirs()


@pytest.fixture(scope="module")
def log_file(api):
    return api.raw_logs.clicks.list_logs("20160909")[0]


AFFILIATE_KWARGS = {
    "company": "Test Company",
    "country": "USA",
    "region": "Ohio",
    "zipcode": "12345",
}


@pytest.fixture(scope="module")
def affiliate(api):
    return api.affiliates.create(**AFFILIATE_KWARGS)


@pytest.fixture(scope="module")
def affiliate_with_user(api):
    """Returns fixture method in order to call it explicitly in tests.

    :return: affiliate fixture method
    """
    user_params = {
        "phone": "+78912345678",
        "first_name": "TestName",
        "last_name": "TestLastName",
        "email": "test7@test.com",
        "password": "123qwe",
        "password_confirmation": "123qwe",
    }
    return api.affiliates.create_with_user(user_params, **AFFILIATE_KWARGS)


@pytest.fixture(scope="module")
def offer_file(api):
    return api.offer_files.create(
        "test/files/test-thumbnail.jpg",
        display="TEST_FILE",
        type="offer thumbnail",
        width=200,
        height=100,
        offer_id=438,
    )


@pytest.fixture(scope="module")
def tag(api):
    return api.tags.create(
        name="test_tag_2",
        offer_applicable=1,
        affiliate_applicable=1,
        advertiser_applicable=1,
        active=1,
        pi_visible=1,
        attribute="Custom",
    )
