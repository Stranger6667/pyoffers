# coding: utf-8


class Model:
    """
    Abstract model for HasOffers entity.
    """
    non_model_fields = ()

    def __init__(self, manager, **kwargs):
        self._manager = manager
        self._data = kwargs

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self._data.get('id'))

    def __repr__(self):
        return '<%s>' % self

    def __getitem__(self, item):
        return self._data[item]

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self['id'] == other['id']


class ModelManager:
    """
    Proxy for API methods with predefined model.
    Used to structure API. Every manager works only with single model methods.
    """
    model = None
    name = None

    def __init__(self, api):
        self.api = api

    def init_instance(self, data):
        return self.model(manager=self, **data)

    def _call(self, method, **kwargs):
        return self.api._call(self.model.__name__, method, **kwargs)
