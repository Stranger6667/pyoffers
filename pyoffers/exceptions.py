# coding: utf-8


class HasOffersException(BaseException):
    pass


class InputError(HasOffersException):
    pass


def check_errors(errors):
    """
    Handles HasOffers errors.
    """
    if not errors:
        return
    raise InputError(errors)
