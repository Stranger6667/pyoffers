# coding: utf-8
from functools import singledispatch
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


def add_query_params(url, **kwargs):
    """
    Adds extra querystring parameters to given URL.
    """
    parsed = list(urlparse(url))
    get_args = parse_qsl(parsed[4]) + [
        (sub_key, sub_value)
        for key, value in kwargs.items()
        for sub_key, sub_value in expand(value, key)
        if sub_value is not None
    ]
    parsed[4] = urlencode(get_args)
    return urlunparse(parsed)


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
        yield key, inner_value
