# coding: utf-8
import pytest
from requests import HTTPError

from pyoffers.exceptions import InvalidPathError

from .responses import INVALID_PATH


@pytest.mark.response(INVALID_PATH)
def test_invalid_path(api):
    with pytest.raises(InvalidPathError):
        api._call('test', 'test')


@pytest.mark.response(status_code=500)
def test_server_error(api):
    with pytest.raises(HTTPError):
        api._call('test', 'test')
