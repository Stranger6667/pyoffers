# coding: utf-8
import os

import pytest

from betamax import Betamax
from betamax_serializers import pretty_json
from pyoffers.api import HasOffersAPI

from .helpers import replace_real_credentials


Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

URL = 'http://www.example.com'
CASSETTE_DIR = 'tests/cassettes/'
DEFAULT_NETWORK_TOKEN = 'token'
DEFAULT_NETWORK_ID = 'id'
NETWORK_TOKEN = os.environ.get('NETWORK_TOKEN', DEFAULT_NETWORK_TOKEN)
NETWORK_ID = os.environ.get('NETWORK_ID', DEFAULT_NETWORK_ID)


def pytest_addoption(parser):
    parser.addoption('--record', action='store_true', help='Runs cleanup for recording session')


def pytest_unconfigure(config):
    if config.getoption('--record'):
        replace_real_credentials(CASSETTE_DIR, NETWORK_TOKEN, DEFAULT_NETWORK_TOKEN, NETWORK_ID, DEFAULT_NETWORK_ID)


@pytest.yield_fixture(autouse=True, scope='module')
def betamax_recorder(request, api):
    """
    Module level Betamax recorder.
    """
    if request.config.getoption('--record'):
        record_mode = 'new_episodes'
    else:
        record_mode = 'none' if os.environ.get('TRAVIS') else 'once'
    cassette_name = getattr(request.node._obj, 'CASSETTE_NAME', 'default')
    vcr = Betamax(
        api.session,
        cassette_library_dir=CASSETTE_DIR,
        default_cassette_options={
            'serialize_with': 'prettyjson',
            'match_requests_on': ['query', 'method'],
            'record_mode': record_mode
        }
    )
    with vcr.use_cassette(cassette_name):
        yield


@pytest.fixture(scope='session')
def api():
    return HasOffersAPI(
        endpoint='https://api.hasoffers.com/Api/json',
        network_token=NETWORK_TOKEN,
        network_id=NETWORK_ID
    )


@pytest.fixture(scope='session')
def advertiser(api):
    return api.advertisers.create(status='pending', company='Test', country='CZ', zipcode='123456')


@pytest.fixture(scope='session')
def offer(api):
    return api.offers.create(
        name='Test', offer_url=URL, status='pending', expiration_date='2030-12-12 23:59:59', preview_url=URL
    )


@pytest.fixture(scope='session')
def conversion(api):
    return api.conversions.create(
        status='pending', payout='1', revenue='1', affiliate_id='1', offer_id='1', status_code='22'
    )


@pytest.fixture(scope='session')
def goal(api):
    offer_instance = offer(api)
    return api.goals.create(name='Test', description='String', status='deleted', offer_id=offer_instance.id)
