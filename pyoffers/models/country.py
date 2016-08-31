# coding: utf-8
from .core import Model, ModelManager


class Country(Model):
    pass


class CountryManager(ModelManager):
    model = Country
    name = 'countries'
