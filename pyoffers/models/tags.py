from pyoffers.utils import Filter

from .core import InvisibleModelManager, Model, ModelManager


class TagRelation(Model):
    """Common model for (Offer|Affiliate|Advertiser)Tag objects.

    These objects just represent relation between tag and corresponding object.
    They are auxiliary objects, hence - no actions on them could be performed directly.
    """


class TagRelationManager(InvisibleModelManager):
    model = TagRelation
    model_aliases = (
        "OffersTags",
        "AffiliatesTags",
        "AdvertisersTags",
    )


class Tag(Model):
    generic_methods = ("update", "delete")
    display_attribute = "name"

    def add_to_offer(self, offer_id):
        return self._manager.add_to_offer(self.id, offer_id=offer_id)

    def add_to_affiliate(self, affiliate_id):
        return self._manager.add_to_affiliate(self.id, affiliate_id=affiliate_id)

    def add_to_advertiser(self, advertiser_id):
        return self._manager.add_to_advertiser(self.id, advertiser_id=advertiser_id)

    def remove_from_offer(self, offer_id):
        return self._manager.remove_from_offer(self.id, offer_id=offer_id)

    def remove_from_affiliate(self, affiliate_id):
        return self._manager.remove_from_affiliate(self.id, affiliate_id=affiliate_id)

    def remove_from_advertiser(self, advertiser_id):
        return self._manager.remove_from_advertiser(self.id, advertiser_id=advertiser_id)


class TagManager(ModelManager):
    model = Tag
    name = "tags"
    generic_methods = (
        "find_by_id",
        "find_all",
        "delete",
        "update",
        "create",
    )

    def find_all_offer_tag_relations(self, **kwargs):
        return self._call(
            "findAllOfferTagRelations", target_class="TagRelation", single_result=False, filters=Filter(**kwargs)
        )

    def find_all_affiliate_tag_relations(self, **kwargs):
        return self._call(
            "findAllAffiliateTagRelations", target_class="TagRelation", single_result=False, filters=Filter(**kwargs)
        )

    def find_all_advertiser_tag_relations(self, **kwargs):
        return self._call(
            "findAllAdvertiserTagRelations", target_class="TagRelation", single_result=False, filters=Filter(**kwargs)
        )

    def add_to_offer(self, tag_id, offer_id):
        return self._call("addToOffer", target_class="TagRelation", tag_id=tag_id, offer_id=offer_id)

    def add_to_affiliate(self, tag_id, affiliate_id):
        return self._call("addToAffiliate", target_class="TagRelation", tag_id=tag_id, affiliate_id=affiliate_id)

    def add_to_advertiser(self, tag_id, advertiser_id):
        return self._call("addToAdvertiser", target_class="TagRelation", tag_id=tag_id, advertiser_id=advertiser_id)

    def set_for_offer(self, tag_ids, offer_id):
        return self._call("setForOffer", target_class="TagRelation", tag_ids=tag_ids, offer_id=offer_id)

    def set_for_affiliate(self, tag_ids, affiliate_id):
        return self._call("setForAffiliate", target_class="TagRelation", tag_ids=tag_ids, affiliate_id=affiliate_id)

    def set_for_advertiser(self, tag_ids, advertiser_id):
        return self._call("setForAdvertiser", target_class="TagRelation", tag_ids=tag_ids, advertiser_id=advertiser_id)

    def remove_from_offer(self, tag_id, offer_id):
        return self._call("removeFromOffer", tag_id=tag_id, offer_id=offer_id)

    def remove_from_affiliate(self, tag_id, affiliate_id):
        return self._call("removeFromAffiliate", tag_id=tag_id, affiliate_id=affiliate_id)

    def remove_from_advertiser(self, tag_id, advertiser_id):
        return self._call("removeFromAdvertiser", tag_id=tag_id, advertiser_id=advertiser_id)

    def remove_from_advertiser_by_relational_id(self, id):
        return self._call("removeFromAdvertiserByRelationalId", id=id)

    def remove_from_offer_by_relational_id(self, id):
        return self._call("removeFromOfferByRelationalId", id=id)

    def remove_from_affiliate_by_relational_id(self, id):
        return self._call("removeFromAffiliateByRelationalId", id=id)
