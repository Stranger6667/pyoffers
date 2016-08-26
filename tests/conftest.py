# coding: utf-8
import pytest
from httmock import HTTMock, all_requests, response

from pyoffers.api import HasOffersAPI
from pyoffers.models import Advertiser


@pytest.fixture
def api():
    return HasOffersAPI(endpoint='https://api.hasoffers.com/Api/json', network_token='token', network_id='id')


@pytest.fixture
def advertiser(api):
    return Advertiser(manager=api.advertisers, id='1', status='pending', company='Test', country='CZ', zipcode='123456')


@pytest.yield_fixture(autouse=True)
def hasoffers_response(request):
    """
    Mocks real HasOffers response with data from `response` mark.
    In case if the mark is absent empty dict is used.
    """
    response_kwargs = {'status_code': 200, 'content': {}}
    marker = request.node.get_marker('response')
    if marker:
        if marker.args:
            response_kwargs['content'] = marker.args[0]
        response_kwargs.update(marker.kwargs)

    @all_requests
    def response_content(url, request):
        instance = response(**response_kwargs)
        instance.json = lambda: response_kwargs['content']
        return instance

    with HTTMock(response_content):
        yield
