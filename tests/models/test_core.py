# coding: utf-8
from unittest.mock import patch

import pytest

from pyoffers.exceptions import HasOffersException


def test_str(advertiser):
    assert str(advertiser) == 'Advertiser: 114'


def test_repr(advertiser):
    assert repr(advertiser) == '<Advertiser: 114>'


@pytest.mark.parametrize(
    'sort, expected', (
        ('id', ['Offer.id']),
        ('Offer.id', ['Offer.id']),
        ('-id', ['-Offer.id']),
        ('-Offer.id', ['-Offer.id']),
        (['-id', 'currency'], ['-Offer.id', 'Offer.currency']),
    )
)
def test_sort_prepend_model(api, sort, expected):
    with patch.object(api, '_call') as patched:
        api.offers.find_all(sort=sort)
        patched.assert_called_with(
            'Offer', 'findAll', contain=None, fields=None, filters={}, limit=None,
            page=None, single_result=False, sort=expected
        )


def test_as_dict(advertiser):
    assert advertiser.as_dict() == {
        'AFFILIATE_NETWORK_Brands_id': None,
        'SHARED_Accounts_id': None,
        'SHARED_Network_Map_id': None,
        '_NETWORK_affiliate_id': None,
        '_NETWORK_affiliate_status': None,
        '_NETWORK_brand_active': '1',
        'account_manager_id': None,
        'address1': None,
        'address2': None,
        'city': None,
        'company': 'Test',
        'conversion_security_token': None,
        'country': 'CZ',
        'date_added': '2016-08-26 08:53:20',
        'expose_subs': '0',
        'fax': None,
        'id': '114',
        'modified': -62169966000,
        'other': None,
        'phone': None,
        'ref_id': None,
        'region': None,
        'signup_ip': None,
        'status': 'pending',
        'tmp_token': None,
        'wants_alerts': '1',
        'website': None,
        'zipcode': '123456'
    }


@pytest.mark.parametrize('value, expected', (
    (
        {'limit': 'a'}, 'Limit should be an integer'
    ),
    (
        {'page': 'a'}, 'Page should be an integer'
    ),
    (
        {'fields': 1}, 'Fields should be a tuple or list'
    ),
))
def test_type_checks(api, value, expected):
    with pytest.raises(AssertionError) as exc:
        api.offers.find_all(**value)
    assert str(exc.value) == expected
