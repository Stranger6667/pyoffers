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


class Filter(dict):
    """
    Custom subtype to apply special behaviour.
    """

    def __init__(self, connector='AND', **kwargs):
        self.connector = connector
        super().__init__(**kwargs)


class Sort(list):
    """
    Handles sort queries.
    """

    def __init__(self, args, model):
        if not isinstance(args, (list, tuple, set)):
            args = [args]
        super().__init__([self.prepend_model(value, model) for value in args])

    def prepend_model(self, value, model):
        """
        Prepends model name if it is not already prepended.
        For example model is "Offer":

            key -> Offer.key
            -key -> -Offer.key
            Offer.key -> Offer.key
            -Offer.key -> -Offer.key
        """
        if '.' not in value:
            direction = ''
            if value.startswith('-'):
                value = value[1:]
                direction = '-'
            value = '%s%s.%s' % (direction, model, value)
        return value


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
        yield '%s[%s]' % (key, dict_key), dict_value


@expand.register(Filter)
def expand_filter(value, key):
    for dict_key, dict_value in value.items():
        if isinstance(dict_value, (list, tuple, set)):
            for sub_value in dict_value:
                yield '%s[%s][]' % (key, dict_key), sub_value
        else:
            try:
                field_name, operator = dict_key.split('__')
                param_name = '%s[%s][%s]' % (key, field_name, OPERATORS[operator])
            except ValueError:
                if value.connector == 'OR':
                    param_name = '%s[%s][%s]' % (key, value.connector, dict_key)
                else:
                    param_name = '%s[%s]' % (key, dict_key)
            yield param_name, dict_value


@expand.register(Sort)
def expand_sort(value, key):
    for field_name in value:
        order = 'asc'
        if field_name.startswith('-'):
            order = 'desc'
            field_name = field_name[1:]
        yield '%s[%s]' % (key, field_name), order


@expand.register(list)
@expand.register(tuple)
@expand.register(set)
def expand_lists(value, key):
    for inner_value in value:
        yield '%s[]' % key, inner_value
