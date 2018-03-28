# coding: utf-8
from .core import Model, ModelManager
from .offer_file import OfferFileManager


class AffiliateUser(Model):
    generic_methods = ('update', 'delete')


class AffiliateUserManager(ModelManager):
    model = AffiliateUser
    name = 'affiliate_users'
    generic_methods = (
        'create',
        'update',
        'delete',
        'find_by_id',
        'find_all',
        'find_all_ids',
    )


class Affiliate(Model):
    """
    An Affiliate.
    """
    generic_methods = ('update', 'delete')

    @property
    def user(self):
        try:
            return AffiliateUserManager(self._manager.api).find_all(affiliate_id=self.id)[0]
        except IndexError:
            return None

    @property
    def files(self):
        return self._get_related_manager(OfferFileManager, 'account_id')

    def block(self, reason=None):
        return self._manager.block(self.id, reason=reason)

    def get_offer_files_with_creative_code(self, offer_id):
        return self._manager.get_offer_files_with_creative_code(self.id, offer_id)


class AffiliateManager(ModelManager):
    model = Affiliate
    name = 'affiliates'
    generic_methods = (
        'update',
        'delete',
        'find_by_id',
        'find_all',
        'find_all_ids',
    )

    def create(self, **kwargs):
        """
        Creates an affiliate
        :param kwargs:
        :return: affiliate instance
        """
        return self._call('create', data=kwargs)

    def create_with_user(self, user_params, **kwargs):
        """
        Creates an affiliate and corresponding affiliate user
        :param user_params: kwargs for user creation
        :param kwargs:
        :return: affiliate instance
        """
        affiliate = self.create(**kwargs)
        self.api.affiliate_users.create(affiliate_id=affiliate.id, **user_params)
        return affiliate

    def block(self, id, reason=None):
        return self._call('block', id=id, reason=reason)

    def get_offer_files_with_creative_code(self, id, offer_id):
        return self._call(
            'getOfferFilesWithCreativeCode',
            target='Offer', target_class='OfferFile', affiliate_id=id, offer_id=offer_id, single_result=False
        )
