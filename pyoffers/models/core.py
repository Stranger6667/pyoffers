# coding: utf-8
from collections import defaultdict

from ..utils import Filter, Sort


class SelectiveInheritanceMeta(type):
    """
    Allows to inherit only methods from `generic_methods` attribute.
    """
    generic_methods = defaultdict(dict)

    def __new__(mcs, name, bases, members):
        if not bases:
            for key, value in list(members.items()):
                if getattr(value, '_is_generic', None):
                    mcs.generic_methods[name][key] = members.pop(key)
        else:
            for method in members.get('generic_methods', ()):
                members[method] = mcs.generic_methods[bases[0].__name__][method]
        return super().__new__(mcs, name, bases, members)


def generic_method(method):
    """
    Marks method as generic.
    """
    method._is_generic = True
    return method


class Model(metaclass=SelectiveInheritanceMeta):
    """
    Abstract model for HasOffers entity.
    """
    generic_methods = ()

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

    @generic_method
    def update(self, **kwargs):
        return self._manager.update(self['id'], **kwargs)


class ModelManager(metaclass=SelectiveInheritanceMeta):
    """
    Proxy for API methods with predefined model.
    Used to structure API. Every manager works only with single model methods.
    """
    model = None
    name = None
    generic_methods = ()

    def __init__(self, api):
        self.api = api

    def init_instance(self, data):
        return self.model(manager=self, **data)

    def _call(self, method, **kwargs):
        return self.api._call(self.model.__name__, method, **kwargs)

    @generic_method
    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    @generic_method
    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    @generic_method
    def find_by_id(self, id, contain=None):
        return self._call('findById', id=id, contain=contain)

    @generic_method
    def find_all(self, sort=(), limit=None, page=None, contain=None, **kwargs):
        return self._call(
            'findAll',
            filters=Filter(**kwargs),
            sort=Sort(sort, self.model.__name__),
            limit=limit, page=page, contain=contain, single_result=False
        )
