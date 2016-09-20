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
        verify=True,
        retries=4,
        retry_timeout=4,
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
``verify``
    Whether to verify SSL certificate or not. HasOffers SSL cert doesn't cover subdomains like mentioned above.
    Only ``*.hasoffers.com`` and ``hasoffers.com``.
``retries``
    Number of retries to make a request in case of exceeding HasOffers API rate limit.
``retry_timeout``
    Seconds to wait between retries.
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

To skip models instantiation you can pass ``raw=True`` to underlying ``_call`` method.
This makes it possible to perform queries without instantiation of model instances.

.. code:: python

    >>> hasoffers.advertisers._call('findAllIds', raw=True)
    ['1', '2', '3', '4']

Managers
~~~~~~~~

- **Advertiser** - ``hasoffers.advertisers``
- **Conversion** - ``hasoffers.conversions``
- **Country** - As the model has no methods then ``hasoffers.countries`` manager has no methods too.
- **Goal** - ``hasoffers.goals``
- **Offer** - ``hasoffers.offers``


Related managers
~~~~~~~~~~~~~~~~

``Offer`` model has ``conversions`` manager, which allows to perform queries on conversions related to concrete offer.

.. code:: python

    >>> offer = hasoffers.offers.find_by_id(7)
    >>> conversions = offer.conversions.find_all()


Raw logs
~~~~~~~~

``pyoffers`` provides ``RawLog`` model with 3 managers for different types of logs. They behave identically:

- ``hasoffers.raw_logs.clicks`` - logs about clicks.
- ``hasoffers.raw_logs.conversions`` - about conversions.
- ``hasoffers.raw_logs.impressions`` - about impressions.

To get all logs directories:

.. code:: python

    >>> hasoffers.raw_logs.clicks.list_date_dirs()
    [<DateDir: Sep 20, 2016 (20160920)>, <DateDir: Sep 19, 2016 (20160919)>, ...]

Every directory has 2 attributes:

- ``displayName``
- ``dirName``

And ``list_logs`` method:

.. code:: python

    >>> directory = hasoffers.raw_logs.clicks.list_date_dirs()[0]
    >>> directory.list_logs()
    [<LogFile: Sep 20, 2016 - 11:00 am (20160920/clicks-1474369200-ewU6Y1.zip)>, ...]

Each log file has:

- ``download_link`` - link to ZIP archive at Amazon S3.
- ``content`` - raw CSV content of this archive.
- ``records`` - all data from CSV wrapped as ``LogRecord`` instances.

All these attributes are cached on ``LogFile`` instance level.
For convenience it is possible to get all records for some date:

.. code:: python

    >>> hasoffers.raw_logs.clicks.find_all('20160920')
    [<LogRecord: 7 (1027a606128bd067105f0b0921840f)>, ...]

Also it is possible to get records for month or even for year. But it will take some time to download all data.

.. code:: python

    >>> september_clicks = hasoffers.raw_logs.clicks.find_all('201609')
    >>> year_clicks = hasoffers.raw_logs.clicks.find_all('2016')