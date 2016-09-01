# coding: utf-8
from unittest.mock import patch

import pytest


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
            'Offer', 'findAll', contain=None, filters={}, limit=None, page=None, single_result=False, sort=expected
        )
