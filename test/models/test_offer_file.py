# coding: utf-8
import pytest

from pyoffers.exceptions import HasOffersException
from pyoffers.models.offer_file import OfferFile

CASSETTE_NAME = "offer_file"


def test_create_success(offer_file):
    assert isinstance(offer_file, OfferFile)
    assert offer_file.display == "TEST_FILE"


def test_create_incorrect_file_path(api):
    with pytest.raises(FileNotFoundError):
        api.offer_files.create(
            "whatever.txt", isplay="TEST_FILE", type="offer thumbnail", width=200, height=100, offer_id=438
        )


def test_find_by_id_success(api, offer_file):
    instance = api.offer_files.find_by_id(offer_file.id)
    assert isinstance(instance, OfferFile)
    assert instance.display == offer_file.display


def test_find_by_id_failure(api):
    assert api.offer_files.find_by_id(902) is None


def test_find_all(api):
    result = api.offer_files.find_all(limit=2)
    assert len(result) == 2
    assert all(isinstance(item, OfferFile) for item in result)


def test_update_success(offer_file):
    new_instance = offer_file.update(display="NEW_TEST_FILE")
    assert new_instance.display == "NEW_TEST_FILE"


def test_update_fail(offer_file):
    with pytest.raises(HasOffersException) as exc:
        offer_file.update(type="whatever")
        assert (
            str(exc.value) == "Error code: 3. Could not update offer file. Type must be one of: file, image banner"
            ", flash banner, email creative, offer thumbnail, text ad, html ad, xml feed, hidden"
        )


def test_delete(offer_file, api):
    offer_file.delete()
    assert api.offer_files.find_by_id(offer_file.id).status == "deleted"


def test_custom_filename(api):
    filename = "another.jpg"
    offer_file = api.offer_files.create(
        "test/files/test-thumbnail.jpg",
        filename=filename,
        display="TEST_FILE",
        type="offer thumbnail",
        width=200,
        height=100,
        offer_id=438,
    )
    assert offer_file.filename == filename


def test_contains_creative_code(api):
    offer_file = api.offer_files.find_by_id(id=2, contain=["CreativeCode"])
    assert offer_file.creativecode == "http://www.example.com"
