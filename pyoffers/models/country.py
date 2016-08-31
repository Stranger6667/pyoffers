# coding: utf-8
from .core import Model, ModelManager


class Country(Model):
    pass


class CountryManager(ModelManager):
    model = Country
    name = 'countries'

    def init_instance(self, data):
        if 'id' not in data:
            data = list(data.values())[0]
        return super().init_instance(data)
