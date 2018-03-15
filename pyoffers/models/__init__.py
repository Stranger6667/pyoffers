# coding: utf-8
from .advertiser import Advertiser, AdvertiserManager  # noqa
from .affiliate import Affiliate, AffiliateManager, AffiliateUser, AffiliateUserManager  # noqa
from .conversion import Conversion, ConversionManager  # noqa
from .core import ApplicationManager, ModelManager  # noqa
from .country import Country, CountryManager  # noqa
from .goal import Goal, GoalManager  # noqa
from .offer import Offer, OfferCategory, OfferCategoryManager, OfferManager  # noqa
from .offer_file import OfferFileManager  # noqa
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
    ApplicationManager,
    OfferFileManager
)

MANAGER_ALIASES = {
    # Some API calls return instances of object under different name. F.e. you have to specify ``contain=['Thumbnail']``
    # in order to find Offer thumbnail (https://developers.tune.com/network/offer-findall/). But it will in fact return
    # ``OfferFile`` instance under ``Thumbnail``. For that we need aliases.
    'Thumbnail': 'OfferFile'
}
