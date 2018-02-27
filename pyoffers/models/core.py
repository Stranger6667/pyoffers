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
        self.__dict__.update(kwargs)

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self._data.get('id'))

    def __repr__(self):
        return '<%s>' % self

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def as_dict(self):
        return self._data

    @generic_method
    def update(self, **kwargs):
        return self._manager.update(self.id, **kwargs)

    @generic_method
    def delete(self, **kwargs):
        return self._manager.delete(self.id)


class ModelManager(metaclass=SelectiveInheritanceMeta):
    """
    Proxy for API methods with predefined model.
    Used to structure API. Every manager works only with single model methods.

    Class properties:
        - model: model class
        - name: a name by which a manager will be referenced in API instance
        - generic_methods: what methods to inherit from base ``ModelManager``
    """
    model = None
    name = None
    generic_methods = ()

    def __init__(self, api):
        self.api = api

    def init_instance(self, data):
        return self.model(manager=self, **data)

    def _call(self, method, **kwargs):
        return self.api._call(self.target, method, **kwargs)

    @property
    def target(self):
        return self.model.__name__

    @generic_method
    def create(self, **kwargs):
        return self._call('create', data=kwargs)

    @generic_method
    def update(self, id, **kwargs):
        return self._call('update', id=id, data=kwargs)

    @generic_method
    def delete(self, id):
        return self.update(id=id, status='deleted')

    @generic_method
    def find_by_id(self, id, fields=None, contain=None):
        assert fields is None or isinstance(fields, (tuple, list)), 'Fields should be a tuple or list'
        return self._call('findById', id=id, fields=fields, contain=contain)

    @generic_method
    def find_all(self, sort=(), limit=None, page=None, fields=None, contain=None, **kwargs):
        assert limit is None or isinstance(limit, int), 'Limit should be an integer'
        assert page is None or isinstance(page, int), 'Page should be an integer'
        assert fields is None or isinstance(fields, (tuple, list)), 'Fields should be a tuple or list'
        return self._call(
            'findAll',
            filters=Filter(**kwargs),
            sort=Sort(sort, self.model.__name__),
            limit=limit, page=page, fields=fields, contain=contain, single_result=False
        )

    @generic_method
    def find_all_ids(self, **kwargs):
        return self._call('findAllIds', filters=Filter(**kwargs), single_result=False, raw=True)


class RelatedManager:
    related_object_name = None

    def __init__(self, api, base_manager_class, id):
        self.base_manager = base_manager_class(api)
        self.id = id

    def find_all(self, **kwargs):
        kwargs[self.related_object_name] = self.id
        return self.base_manager.find_all(**kwargs)


class Application(Model):
    pass


class ApplicationManager(ModelManager):
    """
    Manager for Application controller.

    Ref: https://developers.tune.com/network/application/
    """
    name = 'application'
    model = Application
    target = 'Application'

    def find_all_offer_categories(self, sort=(), fields=None, **kwargs):
        assert fields is None or isinstance(fields, (tuple, list)), 'Fields should be a tuple or list'
        return self._call(
            'findAllOfferCategories',
            filters=Filter(**kwargs),
            sort=sort,
            fields=fields, single_result=False
        )

    def find_all_offer_category_offer_ids(self, id):
        return self._call('findAllOfferCategoryOfferIds', id=id, single_result=False, raw=True)
