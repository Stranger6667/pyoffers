# coding: utf-8
from .core import Model, ModelManager


class Advertiser(Model):
    """
    An Advertiser account.
    """
    generic_methods = ('update',)

    def block(self, reason=''):
        return self._manager.block(self.id, reason)


class AdvertiserManager(ModelManager):
    model = Advertiser
    name = 'advertisers'
    generic_methods = (
        'create',
        'update',
        'find_by_id',
        'find_all',
        'find_all_ids',
    )

    def block(self, id, reason=''):
        return self._call('block', id=id, reason=reason)
