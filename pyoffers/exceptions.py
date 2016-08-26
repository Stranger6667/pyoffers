# coding: utf-8


class HasOffersException(BaseException):
    pass


class InvalidPathError(HasOffersException):
    pass


class InputError(HasOffersException):
    pass


def check_errors(errors):
    """
    Handles HasOffers errors.
    """
    if not errors:
        return
    if isinstance(errors, dict):
        if errors['publicMessage'] == 'Invalid path for URL':
            raise InvalidPathError
    raise InputError(errors)
