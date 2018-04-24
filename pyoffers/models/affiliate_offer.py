from .core import Model, ModelManager


class AffiliateOffer(Model):
    """"
    Model that defines relation between Offer and Affiliate
    """
    pass


class AffiliateOfferManager(ModelManager):
    model = AffiliateOffer
    name = 'affiliate_offers'
