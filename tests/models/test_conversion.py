# coding: utf-8
from pyoffers.models import Conversion


CASSETTE_NAME = 'conversion'


def test_create_success(conversion):
    assert isinstance(conversion, Conversion)
    assert conversion['revenue'] == '1.00000'


def test_find_by_id_success(api, conversion):
    instance = api.conversions.find_by_id(conversion['id'])
    assert isinstance(instance, Conversion)
    assert instance['revenue'] == conversion['revenue']


def test_find_by_id_fail(api):
    assert api.conversions.find_by_id(100000) is None


def test_find_all(api):
    result = api.conversions.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Conversion) for item in result)


def test_update_success(conversion):
    conversion['revenue'] = '2'
    new_instance = conversion.update()
    assert new_instance['revenue'] == '2.00000'
    assert new_instance == conversion
