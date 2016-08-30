# coding: utf-8
from functools import singledispatch


def prepare_query_params(**kwargs):
    """
    Prepares given parameters to be used in querystring.
    """
    return [
        (sub_key, sub_value)
        for key, value in kwargs.items()
        for sub_key, sub_value in expand(value, key)
        if sub_value is not None
    ]

OPERATORS = {
    'ne': 'NOT_EQUAL_TO',
    'lt': 'LESS_THAN',
    'lte': 'LESS_THAN_OR_EQUAL_TO',
    'gt': 'GREATER_THAN',
    'gte': 'GREATER_THAN_OR_EQUAL_TO',
    'like': 'LIKE',
    'not_like': 'NOT_LIKE',
    'null': 'NULL',
    'not_null': 'NOT_NULL',
    'true': 'TRUE',
    'false': 'FALSE',
}


@singledispatch
def expand(value, key):
    yield key, value


@expand.register(dict)
def expand_dict(value, key):
    for dict_key, dict_value in value.items():
        if isinstance(dict_value, (list, tuple, set)):
            for sub_value in dict_value:
                yield '%s[%s][]' % (key, dict_key), sub_value
        else:
            try:
                field_name, operator = dict_key.split('__')
                yield '%s[%s][%s]' % (key, field_name, OPERATORS[operator]), dict_value
            except ValueError:
                yield '%s[%s]' % (key, dict_key), dict_value


@expand.register(list)
@expand.register(tuple)
@expand.register(set)
def expand_lists(value, key):
    for inner_value in value:
        yield '%s[]' % key, inner_value
