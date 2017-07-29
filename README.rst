PyOffers
========

.. image:: https://travis-ci.org/Stranger6667/pyoffers.svg?branch=master
   :target: https://travis-ci.org/Stranger6667/pyoffers
   :alt: Build Status

.. image:: https://codecov.io/github/Stranger6667/pyoffers/coverage.svg?branch=master
   :target: https://codecov.io/github/Stranger6667/pyoffers?branch=master
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/pyoffers/badge/?version=latest
   :target: http://pyoffers.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Python client library for `HasOffers API <http://developers.hasoffers.com/>`_.

Installation
============

PyOffers can be obtained with ``pip``::

    $ pip install pyoffers

Usage example
=============

Initialize API client:

.. code-block:: python

    >>> from pyoffers.api import HasOffersAPI
    >>> hasoffers = HasOffersAPI(
        endpoint='https://api.hasoffers.com/Apiv3/json',
        network_token='<your_network_token>',
        network_id='<your_network_id>',
    )

Execute queries:

.. code-block:: python

    >>> # Get all offers with ID greater than 100, sorted by ID and with loaded `Country` data
    >>> hasoffers.offers.find_all(id__gt=100, sort='id', contain=['Country'])
    [<Offer: 102>,
 <Offer: 104>,
 <Offer: 106>,
 <Offer: 108>,
 <Offer: 110>,
 <Offer: 112>]
    >>> # Get all clicks records for 2016-09-20
    >>> hasoffers.raw_logs.clicks.find_all('20160920')
    [<LogRecord: 7 (1027a606128bd067105f0b0921840f)>, ...]
    >>> # Get all conversions for specific offer
    >>> offer = hasoffers.offers.get_by_id(100)
    >>> offer.conversions.find_all()
    [<Conversion: 70532>]


Documentation
=============

You can view documentation online at:

- https://pyoffers.readthedocs.io

Or you can look at the docs/ directory in the repository.

Python support
==============

PyOffers supports Python 3.4+.
