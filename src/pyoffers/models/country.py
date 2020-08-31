from .core import Model, ModelManager


class Country(Model):
    display_attribute = "code"


class CountryManager(ModelManager):
    model = Country
    name = "countries"
