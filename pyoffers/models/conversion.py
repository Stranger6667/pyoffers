# coding: utf-8
from .core import Model, ModelManager


class Conversion(Model):
    """
    A Conversion.
    """
    non_model_fields = ('internal_ad_id', )

    def update(self, **kwargs):
        return self._manager.update(self['id'], **kwargs)


class ConversionManager(ModelManager):
    model = Conversion
    name = 'conversions'

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    def find_by_id(self, id, contain=None):
        return self._call('findById', id=id, contain=contain)

    def find_all(self, sort=None, limit=None, page=None, contain=None, **kwargs):
        return self._call(
            'findAll', filters=kwargs, sort=sort, limit=limit, page=page, contain=contain, single_result=False
        )
