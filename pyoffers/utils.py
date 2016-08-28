# coding: utf-8
from functools import singledispatch


def prepare_query_params(**kwargs):
    """
    Adds extra querystring parameters to given URL.
    """
    return {
        sub_key: sub_value
        for key, value in kwargs.items()
        for sub_key, sub_value in expand(value, key)
        if sub_value is not None
    }


@singledispatch
def expand(value, key):
    yield key, value


@expand.register(dict)
def expand_dict(value, key):
    for inner_key, inner_value in value.items():
        yield '%s[%s]' % (key, inner_key), inner_value


@expand.register(list)
@expand.register(tuple)
def expand_lists(value, key):
    for inner_value in value:
        yield '%s[]' % key, inner_value
