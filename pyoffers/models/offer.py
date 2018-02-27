# coding: utf-8
from .conversion import ConversionManager
from .core import ApplicationManager, Model, ModelManager, RelatedManager


class RelatedConversionsManager(RelatedManager):
    related_object_name = 'offer_id'


class Offer(Model):
    """
    An Offer.
    """
    generic_methods = ('update',)

    @property
    def conversions(self):
        return RelatedConversionsManager(api=self._manager.api, base_manager_class=ConversionManager, id=self.id)

    def add_target_country(self, country_code):
        return self._manager.add_target_country(self.id, country_code)

    def get_target_countries(self):
        return self._manager.get_target_countries(self.id)

    def add_category(self, category_id):
        return self._manager.add_category(self.id, category_id)

    def block_affiliate(self, affiliate_id):
        return self._manager.block_affiliate(self.id, affiliate_id)

    def get_categories(self):
        return self._manager.get_categories(self.id)


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

    def block_affiliate(self, id, affiliate_id):
        return self._call('blockAffiliate', id=id, affiliate_id=affiliate_id)

    def get_categories(self, id):
        return self._call('getCategories', id=id, single_result=False)


class OfferCategory(Model):
    """"
    Offer category
    """
    generic_methods = (
        'update',
    )


class OfferCategoryManager(ApplicationManager):
    """
    This manager doesn't inherit any generic method, since it operates on an Application model
    """
    model = OfferCategory

    def update(self, id, **kwargs):
        return self._call('updateOfferCategory', id=id, data=kwargs)
