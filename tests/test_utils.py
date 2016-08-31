# coding: utf-8
import pytest

from pyoffers.utils import expand, Filter


@pytest.mark.parametrize(
    'value, expected',
    (
        (
            (1, 'key'),
            {('key', 1)}
        ),
        (
            ([1, 2, 3], 'key'),
            {('key[]', 1), ('key[]', 2), ('key[]', 3)}
        ),
        (
            ({'a': 1, 'b': 2}, 'key'),
            {('key[a]', 1), ('key[b]', 2)}
        ),
        (
            (Filter(status=('active', 'paused'), currency='USD'), 'filters'),
            {('filters[status][]', 'active'), ('filters[status][]', 'paused'), ('filters[currency]', 'USD')}
        ),
        (
            (Filter(id__lt=25), 'filters'),
            {('filters[id][LESS_THAN]', 25)}
        ),
        (
            (Filter(status='active', currency='USD', connector='OR'), 'filters'),
            {('filters[OR][status]', 'active'), ('filters[OR][currency]', 'USD')}
        ),
    )
)
def test_expand(value, expected):
    assert set(expand(*value)) == expected
