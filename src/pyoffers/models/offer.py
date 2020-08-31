from pyoffers.utils import Filter

from .conversion import ConversionManager
from .core import ApplicationManager, Model, ModelManager
from .offer_file import OfferFileManager


class Offer(Model):
    """An Offer."""

    generic_methods = ("update",)
    related_object_name = "offer_id"
    display_attribute = "name"

    @property
    def conversions(self):
        return self._get_related_manager(ConversionManager)

    @property
    def files(self):
        return self._get_related_manager(OfferFileManager)

    def add_target_country(self, country_code):
        return self._manager.add_target_country(self.id, country_code)

    def get_target_countries(self):
        return self._manager.get_target_countries(self.id)

    def add_category(self, category_id):
        return self._manager.add_category(self.id, category_id)

    def block_affiliate(self, affiliate_id):
        return self._manager.block_affiliate(self.id, affiliate_id)

    def unblock_affiliate(self, affiliate_id):
        return self._manager.unblock_affiliate(self.id, affiliate_id)

    def get_categories(self):
        return self._manager.get_categories(self.id)

    def get_offer_files_with_creative_code(self, affiliate_id):
        return self._manager.get_offer_files_with_creative_code(self.id, affiliate_id)

    def set_affiliate_approval_status(self, affiliate_id, status):
        return self._manager.set_affiliate_approval_status(self.id, affiliate_id, status)

    def get_affiliate_approval_status(self, affiliate_id):
        return self._manager.get_affiliate_approval_status(self.id, affiliate_id)

    def get_blocked_affiliate_ids(self):
        return self._manager.get_blocked_affiliate_ids(self.id)

    def get_approved_affiliate_ids(self):
        return self._manager.get_approved_affiliate_ids(self.id)

    def get_unapproved_affiliate_ids(self):
        return self._manager.get_unapproved_affiliate_ids(self.id)

    def generate_tracking_link(self, affiliate_id, tiny_url=False, **params):
        return self._manager.generate_tracking_link(self.id, affiliate_id, tiny_url=tiny_url, **params)

    def find_all_affiliate_approvals(self, sort=(), limit=None, page=None, fields=None, **kwargs):
        kwargs["offer_id"] = self.id
        return self._manager.find_all_affiliate_approvals(sort=(), limit=None, page=None, fields=None, **kwargs)


class OfferManager(ModelManager):
    model = Offer
    name = "offers"
    generic_methods = (
        "create",
        "update",
        "find_by_id",
        "find_all",
        "find_all_ids",
    )

    def add_target_country(self, id, country_code):
        return self._call("addTargetCountry", id=id, country_code=country_code)

    def get_target_countries(self, id):
        return self._call("getTargetCountries", id=id, single_result=False)

    def add_category(self, id, category_id):
        return self._call("addCategory", id=id, category_id=category_id)

    def block_affiliate(self, id, affiliate_id):
        return self._call("blockAffiliate", id=id, affiliate_id=affiliate_id)

    def unblock_affiliate(self, id, affiliate_id):
        return self._call("unblockAffiliate", id=id, affiliate_id=affiliate_id)

    def get_categories(self, id):
        return self._call("getCategories", id=id, single_result=False)

    def get_offer_files_with_creative_code(self, id, affiliate_id):
        return self._call(
            "getOfferFilesWithCreativeCode",
            target_class="OfferFile",
            affiliate_id=affiliate_id,
            offer_id=id,
            single_result=False,
        )

    def set_affiliate_approval_status(self, id, affiliate_id, status):
        return self._call(
            "setAffiliateApproval", id=id, affiliate_id=affiliate_id, status=status, target_class="AffiliateOffer"
        )

    def get_affiliate_approval_status(self, id, affiliate_id):
        return self._call("getAffiliateApprovalStatus", id=id, affiliate_id=affiliate_id, raw=True)

    def get_blocked_affiliate_ids(self, id):
        return self._call("getBlockedAffiliateIds", id=id, raw=True)

    def get_approved_affiliate_ids(self, id):
        return self._call("getApprovedAffiliateIds", id=id, raw=True)

    def get_unapproved_affiliate_ids(self, id):
        return self._call("getUnapprovedAffiliateIds", id=id, raw=True)

    def generate_tracking_link(self, id, affiliate_id, tiny_url=False, **params):
        tiny_url = "1" if tiny_url else "0"
        return self._call(
            "generateTrackingLink",
            offer_id=id,
            affiliate_id=affiliate_id,
            options={"tiny_url": tiny_url},
            params=params,
            raw=True,
        )

    def find_all_affiliate_approvals(self, sort=(), limit=None, page=None, fields=None, **kwargs):
        return self._call(
            "findAllAffiliateApprovals",
            sort=sort,
            limit=limit,
            page=page,
            fields=fields,
            single_result=False,
            target_class="AffiliateOffer",
            filters=Filter(**kwargs),
        )


class OfferCategory(Model):
    """Offer category."""

    generic_methods = ("update",)


class OfferCategoryManager(ApplicationManager):

    model = OfferCategory

    def update(self, id, **kwargs):
        return self._call("updateOfferCategory", id=id, data=kwargs)
