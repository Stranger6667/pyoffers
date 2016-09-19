# coding: utf-8


def format_error(error):
    if 'publicMessage' in error and len(error) == 1:
        return error['publicMessage']
    elif 'publicMessage' not in error:
        return 'Error code: %s. %s' % (error['err_code'], error['err_msg'])
    return 'Error code: %s. %s %s' % (error['err_code'], error['publicMessage'], error['err_msg'])


class HasOffersException(BaseException):

    def __str__(self):
        return '\n'.join(format_error(error) for error in self.errors)

    @property
    def errors(self):
        value = self.args[0]
        if not isinstance(value, list):
            value = [value]
        return value


class MaxRetriesExceeded(HasOffersException):

    def __str__(self):
        return 'Max retries exceeded'
