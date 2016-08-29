# coding: utf-8


def test_str(advertiser):
    assert str(advertiser) == 'Advertiser: 114'


def test_repr(advertiser):
    assert repr(advertiser) == '<Advertiser: 114>'
