# coding: utf-8
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


def add_get_args(url, **kwargs):
    parsed = list(urlparse(url))
    get_args = parse_qsl(parsed[4])
    for key, value in kwargs.items():
        if not isinstance(value, (list, tuple, dict)):
            if value is not None:
                get_args.append((key, value))
        elif isinstance(value, dict):
            for inner_key, inner_value in value.items():
                if inner_value is not None:
                    arg_key = '%s[%s]' % (key, inner_key)
                    get_args.append((arg_key, inner_value))
        else:
            for inner_value in value:
                if inner_value is not None:
                    get_args.append((key, inner_value))
    parsed[4] = urlencode(get_args)
    return urlunparse(parsed)
