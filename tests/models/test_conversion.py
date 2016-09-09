# coding: utf-8
from pyoffers.models import Conversion


CASSETTE_NAME = 'conversion'


def test_create_success(conversion):
    assert isinstance(conversion, Conversion)
    assert conversion.revenue == '1.00000'


def test_find_by_id_success(api, conversion):
    instance = api.conversions.find_by_id(conversion.id)
    assert isinstance(instance, Conversion)
    assert instance.revenue == conversion.revenue


def test_find_by_id_fail(api):
    assert api.conversions.find_by_id(100000) is None


def test_find_all(api):
    result = api.conversions.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, Conversion) for item in result)


def test_find_all_not_paginated(api):
    result = api.conversions.find_all(offer_id=9)
    assert len(result) == 2
    assert all(isinstance(item, Conversion) for item in result)


def test_find_all_single_result(api):
    result = api.conversions.find_all(offer_id=7, source='FP', status='approved', session_ip='127.0.0.1')
    assert len(result) == 1
    assert isinstance(result[0], Conversion)


def test_find_all_not_paginated_not_found(api):
    assert api.conversions.find_all(offer_id=11) == []


def test_find_all_not_found(api):
    assert api.conversions.find_all(goal_id=100000, limit=1) == []


def test_update_success(conversion):
    new_instance = conversion.update(revenue=2)
    assert new_instance.revenue == '2.00000'
    assert new_instance == conversion
