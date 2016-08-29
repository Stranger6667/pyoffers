# coding: utf-8
from .core import Model, ModelManager


class Advertiser(Model):
    """
    An Advertiser account.
    """

    def update(self):
        return self._manager.update(**self.instance_data)

    def block(self, reason=''):
        return self._manager.block(self['id'], reason)


class AdvertiserManager(ModelManager):
    model = Advertiser

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    def find_by_id(self, id):
        return self._call('findById', id=id)

    def block(self, id, reason=''):
        return self._call('block', id=id, reason=reason)
