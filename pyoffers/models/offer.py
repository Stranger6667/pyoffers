# coding: utf-8
from .core import Model, ModelManager


class Offer(Model):
    """
    An Offer.
    """
    non_model_fields = ('dne_third_party_list', )

    def update(self):
        return self._manager.update(**self.instance_data)

    def add_target_country(self, country_code):
        return self._manager.add_target_country(self['id'], country_code)

    def add_category(self, category_id):
        return self._manager.add_category(self['id'], category_id)


class OfferManager(ModelManager):
    model = Offer

    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    def find_by_id(self, id):
        return self._call('findById', id=id)

    def add_target_country(self, id, country_code):
        return self._call('addTargetCountry', id=id, country_code=country_code)

    def add_category(self, id, category_id):
        return self._call('addCategory', id=id, category_id=category_id)
