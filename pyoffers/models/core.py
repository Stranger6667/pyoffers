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

    def __setitem__(self, key, value):
        self._data[key] = value

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self['id'] == other['id']

    @property
    def instance_data(self):
        """
        All data except for private and non model fields.
        """
        return {
            key: value for key, value in self._data.items()
            if not key.startswith('_') and key not in self.non_model_fields
        }


class ModelManager:
    """
    Proxy for API methods with predefined model.
    Used to structure API. Every manager works only with single model methods.
    """
    model = None

    def bind(self, api):
        self.api = api

    def init_instance(self, data):
        return self.model(manager=self, **data)

    def _call(self, method, **kwargs):
        return self.api._call(self.model.__name__, method, **kwargs)
