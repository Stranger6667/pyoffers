# coding: utf-8
import pytest

from pyoffers.utils import expand


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
        )
    )
)
def test_expand(value, expected):
    assert set(expand(*value)) == expected
