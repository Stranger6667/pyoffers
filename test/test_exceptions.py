import pytest

from pyoffers.exceptions import HasOffersException


@pytest.mark.parametrize(
    "errors, expected",
    (
        (
            [
                {
                    "err_code": 1,
                    "err_msg": "Name cannot be blank.",
                    "attribute_name": "name",
                    "publicMessage": "Could not create offer.",
                },
                {"err_code": 1, "err_msg": "Preview_url cannot be blank.", "attribute_name": "preview_url"},
                {"err_code": 1, "err_msg": "Offer_url cannot be blank.", "attribute_name": "offer_url"},
                {"err_code": 1, "err_msg": "Expiration_date cannot be blank.", "attribute_name": "expiration_date"},
            ],
            "Error code: 1. Could not create offer. Name cannot be blank.\n"
            "Error code: 1. Preview_url cannot be blank.\n"
            "Error code: 1. Offer_url cannot be blank.\n"
            "Error code: 1. Expiration_date cannot be blank.",
        ),
        ([{"publicMessage": "Row id is negative"}], "Row id is negative"),
        (
            {
                "attribute_name": "account_manager_id",
                "err_code": 3,
                "err_msg": "Account_manager_id is not valid.",
                "publicMessage": "Could not update advertiser.",
            },
            "Error code: 3. Could not update advertiser. Account_manager_id is not valid.",
        ),
    ),
)
def test_representation(errors, expected):
    assert str(HasOffersException(errors)) == expected
