# coding: utf-8
from .core import Model, ModelManager


class Offer(Model):
    """
    An Offer.
    """
    generic_methods = ('update',)

    def add_target_country(self, country_code):
        return self._manager.add_target_country(self['id'], country_code)

    def get_target_countries(self):
        return self._manager.get_target_countries(self['id'])

    def add_category(self, category_id):
        return self._manager.add_category(self['id'], category_id)


class OfferManager(ModelManager):
    model = Offer
    name = 'offers'
    generic_methods = (
        'create',
        'update',
        'find_by_id',
        'find_all',
        'find_all_ids',
    )

    def add_target_country(self, id, country_code):
        return self._call('addTargetCountry', id=id, country_code=country_code)

    def get_target_countries(self, id):
        return self._call('getTargetCountries', id=id, single_result=False)

    def add_category(self, id, category_id):
        return self._call('addCategory', id=id, category_id=category_id)
