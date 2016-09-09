# coding: utf-8
from .advertiser import Advertiser, AdvertiserManager
from .conversion import Conversion, ConversionManager
from .core import ModelManager
from .country import Country, CountryManager
from .goal import Goal, GoalManager
from .offer import Offer, OfferManager
from .raw_log import RawLogManager


MODEL_MANAGERS = (
    AdvertiserManager, ConversionManager, CountryManager, GoalManager, OfferManager, RawLogManager
)
