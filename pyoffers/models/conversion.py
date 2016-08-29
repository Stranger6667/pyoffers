# coding: utf-8
from .core import Model, ModelManager


class Conversion(Model):
    """
    A Conversion.
    """
    non_model_fields = ('internal_ad_id', )

    def update(self):
        return self._manager.update(**self.instance_data)


class ConversionManager(ModelManager):
    model = Conversion

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    def find_by_id(self, id):
        return self._call('findById', id=id)

    def find_all(self, filters=None, sort=None, limit=None, page=None):
        return self._call('findAll', filters=filters, sort=sort, limit=limit, page=page)
