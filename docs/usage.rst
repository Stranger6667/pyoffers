.. _usage:

Usage
=====

Basic
-----

PyOffers provide ``HasOffersAPI`` class to interact with HasOffers API.

.. code:: python

    from pyoffers.api import HasOffersAPI


    hasoffers = HasOffersAPI(
        endpoint='https://api.hasoffers.com/Apiv3/json',
        network_token='<your_network_token>',
        network_id='<your_network_id>',
        verbosity=3
    )

Possible options:

``endpoint``
    URL, which points to HasOffers server.
    It may contain your subdomain as well - ``https://<your_subdomain>.api.hasoffers.com/Apiv3/json``
``network_token``
    Your NetworkToken.
``network_id``
    Your NetworkId.
``verbosity``
    Controls library's verbosity level. With **3** the request params and raw response will be printed to console.

With this class instance you can perform requests to the API.

Models
------

The core idea of interaction with model is based on managers.
To work with HasOffers data model you should use appropriate manager.
For now only very limited part of models are presented.

Core managers methods
~~~~~~~~~~~~~~~~~~~~~

.. function:: create(self, **kwargs)

Just pass model data as ``kwargs`` to create new instance of model. The new instance will be returned.

.. function:: update(self, id, **kwargs)

Takes ``id`` of existing model instance and new data as ``kwargs``. Updated instance will be returned.

.. function:: find_by_id(self, id, contain=None)

If you pass related models names to ``contain`` argument, then if related model exists it will be attached to the
returned object as its attribute.

.. code:: python

    >>> offer = hasoffers.offers.find_by_id(id=62, contain=['Country'])
    >>> print(offer.country)
    <Country: 724>

.. function:: find_all(self, sort=(), limit=None, page=None, contain=None, **kwargs)

``sort`` can be a single field name or list of them. To sort in descending order put ``-`` before the field name.

.. code:: python

    >>> hasoffers.offers.find_all(sort='-id')
    [<Offer: 9>,
     <Offer: 7>,
     <Offer: 5>,
     <Offer: 3>,
     <Offer: 1>]

There are some extra features to make advanced queries.
To use different operators you should append its name to the end of the field_name.
Example. To get all offers with ``id`` greater than 100:

.. code:: python

    >>> hasoffers.offers.find_all(id__gt=100, sort='id')
    [<Offer: 102>,
     <Offer: 104>,
     <Offer: 106>,
     <Offer: 108>,
     <Offer: 110>,
     <Offer: 112>]

PyOffers supports the following operators:

- ``ne`` - ``NOT_EQUAL_TO``
- ``lt`` - ``LESS_THAN``
- ``lte`` - ``LESS_THAN_OR_EQUAL_TO``
- ``gt`` - ``GREATER_THAN``
- ``gte`` - ``GREATER_THAN_OR_EQUAL_TO``
- ``like`` - ``LIKE``
- ``not_like`` - ``NOT_LIKE``
- ``null`` - ``NULL``
- ``not_null`` - ``NOT_NULL``
- ``true`` - ``TRUE``
- ``false`` - ``FALSE``

To perform ``OR`` queries pass ``connector='OR'`` as filter.
To get all offers with **active** status OR with **USD** currency:

.. code:: python

    >>> hasoffers.offers.find_all(status='active', currency='USD', connector='OR')

Managers
~~~~~~~~

- **Advertiser** - ``hasoffers.advertisers``
- **Conversion** - ``hasoffers.conversions``
- **Country** - As the model has no methods then ``hasoffers.countries`` manager has no methods too.
- **Goal** - ``hasoffers.goals``
- **Offer** - ``hasoffers.offers``
