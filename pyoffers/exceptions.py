# coding: utf-8


class HasOffersException(BaseException):
    pass


class NetworkIDError(HasOffersException):
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
        if errors['publicMessage'] == 'Network id is not valid':
            raise NetworkIDError(errors['publicMessage'])
        if errors['publicMessage'] == 'Invalid path for URL':
            raise InvalidPathError(errors['publicMessage'])
    raise InputError(errors)
