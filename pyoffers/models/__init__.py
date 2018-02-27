# coding: utf-8
from .advertiser import Advertiser, AdvertiserManager  # noqa
from .affiliate import Affiliate, AffiliateManager, AffiliateUser, AffiliateUserManager  # noqa
from .conversion import Conversion, ConversionManager  # noqa
from .core import ApplicationManager, ModelManager  # noqa
from .country import Country, CountryManager  # noqa
from .goal import Goal, GoalManager  # noqa
from .offer import Offer, OfferCategory, OfferCategoryManager, OfferManager  # noqa
from .raw_log import RawLogManager  # noqa


MODEL_MANAGERS = (
    AdvertiserManager,
    ConversionManager,
    CountryManager,
    GoalManager,
    OfferManager,
    RawLogManager,
    AffiliateManager,
    AffiliateUserManager,
    OfferCategoryManager,
    ApplicationManager
)
