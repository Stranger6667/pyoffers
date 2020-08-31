PyOffers
========

|Build| |Coverage| |Version| |Python versions| |License|

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

PyOffers supports Python 3.5+.

.. |Build| image:: https://github.com/Stranger6667/pyoffers/workflows/build/badge.svg
   :target: https://github.com/Stranger6667/pyoffers/actions
.. |Coverage| image:: https://codecov.io/github/Stranger6667/pyoffers/coverage.svg?branch=master
    :target: https://codecov.io/github/Stranger6667/pyoffers?branch=master
.. |Version| image:: https://img.shields.io/pypi/v/pyoffers.svg
   :target: https://pypi.org/project/pyoffers/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/pyoffers.svg
   :target: https://pypi.org/project/pyoffers/
.. |License| image:: https://img.shields.io/pypi/l/pyoffers.svg
   :target: https://opensource.org/licenses/MIT
