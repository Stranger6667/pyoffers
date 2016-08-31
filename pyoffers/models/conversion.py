# coding: utf-8
from .core import Model, ModelManager


class Conversion(Model):
    """
    A Conversion.
    """
    generic_methods = ('update', )


class ConversionManager(ModelManager):
    model = Conversion
    name = 'conversions'
    generic_methods = (
        'create',
        'update',
        'find_by_id',
        'find_all',
    )
