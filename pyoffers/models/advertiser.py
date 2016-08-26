# coding: utf-8
from .core import Model, ModelManager


class Advertiser(Model):
    """
    An Advertiser account.
    """

    def save(self):
        return self._manager.update(self['id'], **self.instance_data)

    def block(self, reason=''):
        return self._manager.block(self['id'], reason)


class AdvertiserManager(ModelManager):
    model = 'Advertiser'

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, advertiser_id, **kwargs):
        return self._call('update', id=advertiser_id, data=kwargs)

    def find_by_id(self, advertiser_id):
        return self._call('findById', id=advertiser_id)

    def block(self, advertiser_id, reason=''):
        return self._call('block', id=advertiser_id, reason=reason)
