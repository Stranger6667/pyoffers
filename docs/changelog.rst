.. _changelog:

Changelog
=========

`Unreleased`_
-------------

Added
~~~~~

- New related managers ``Offer.files`` and ``Affiliate.files``. (`Stranger6667`_)
- Support for ``CreativeCode`` in ``contains`` list. (`Stranger6667`_)
- ``get_offer_files_with_creative_code`` method for ``Affiliate`` and ``Offer`` models. (`Stranger6667`_)

`0.6.3`_ - 2018-03-15
---------------------

Added
~~~~~

- Support managing of ``OfferFile`` objects. (`iamanikeev`_)

`0.6.2`_ - 2018-03-12
---------------------

Fixed
~~~~~

- Initialization of singular objects from API calls. (`iamanikeev`_)

`0.6.1`_ - 2018-02-28
---------------------

Added
~~~~~

- Introduce ``Application`` model. (`iamanikeev`_)
- Support managing of ``OfferCategory`` objects. (`iamanikeev`_)

Fixed
~~~~~

- Initialization of array of objects from API calls. (`iamanikeev`_)

`0.6.0`_ - 2018-02-20
---------------------

Added
~~~~~

- Support ``blockAffiliate`` method. (`iamanikeev`_)
- Add ``Affiliate`` and ``AffiliateUser`` models. (`iamanikeev`_)
- Recreate session in case of ConnectionReset errors. (`iamanikeev`_)

`0.5.0`_ - 2016-09-20
---------------------

Added
~~~~~
- Added ``fields`` parameter. `#34`_
- Added retrying support on rate limit exceeding. `#43`_
- Added type checks for calls parameters. `#51`_
- Added ``conversions`` manager for ``Offer`` instances. `#48`_

Changed
~~~~~~~

- Better exceptions representation. `#52`_

Fixed
~~~~~

- Fixed credentials cleaning for non gzipped content. `#45`_

`0.4.4`_ - 2016-09-09
---------------------

Changed
~~~~~~~

- Improved logs filtration. `#42`_

`0.4.3`_ - 2016-09-09
---------------------

Added
~~~~~

- Added caching for raw logs. `#41`_
- Added ``RawLog`` model. `#40`_
- Added ``as_dict`` method to models. `#39`_

Changed
~~~~~~~
- Better interface for models. `#38`_

`0.4.2`_ - 2016-09-01
---------------------

Added
~~~~~

- Added ``raw`` argument to ``HasOffersAPI._call``. `#36`_
- Implemented ``findAllIds`` method. `#35`_

Changed
~~~~~~~

- Made SSL certificate verification optional. `#33`_

`0.4.1`_ - 2016-09-01
---------------------

Changed
~~~~~~~

- Improved sorting. `#31`_


Fixed
~~~~~

- Fixed ``contain`` behaviour. `#32`_

`0.4.0`_ - 2016-08-31
---------------------

Added
~~~~~

- Implemented generic methods. `#10`_
- Implemented ``OR`` queries. `#19`_
- Implemented ``sort`` in queries. `#29`_

Changed
~~~~~~~

- Better interface for ``update`` method. `#28`_
- Improved ``contain``. Added ``contain`` support to ``find_by_id`` method. `#27`_

Fixed
~~~~~

- Fixed managers sharing between API instances. `#26`_

`0.3.2`_ - 2016-08-30
---------------------

Added
~~~~~

- Added ``Country`` model. `#24`_
- Added ``get_target_countries`` method to ``Offer`` model. `#25`_

`0.3.1`_ - 2016-08-30
---------------------

Added
~~~~~

- Added ``find_all`` methods for all defined models. `#23`_
- Initial support for ``contain`` in ``find_all`` queries. `#22`_

Changed
~~~~~~~

- Improved logging. `#20`_, `#21`_

`0.3.0`_ - 2016-08-30
---------------------

Added
~~~~~

- Filters implementation. `#6`_

Fixed
~~~~~

- Fixed invalid queries building. `#16`_
- Fixed error on empty not paginated results. `#17`_
- Fixed error on single result in ``find_all`` call. `#18`_

`0.2.2`_ - 2016-08-29
---------------------

Fixed
~~~~~

- Fixed error on not paginated results. `#14`_

`0.2.1`_ - 2016-08-29
---------------------

Fixed
~~~~~

- Don't touch cassette if it contains no production credentials. `#12`_
- Fixed exception if no results were found. `#13`_

`0.2.0`_ - 2016-08-29
---------------------

Added
~~~~~

- Added support for returning multiple objects. `#7`_
- Added ``Conversion`` model. `#3`_
- Better models representation. `#8`_

Changed
~~~~~~~

- Refactored models instantiation. `#9`_

Fixed
~~~~~

- Fixed credentials leak. `#11`_

`0.1.2`_ - 2016-08-29
---------------------

Fixed
~~~~~

- Fixed query building for lists and tuples. `#5`_

`0.1.1`_ - 2016-08-28
---------------------

Fixed
~~~~~

- Fixed packaging issue.

0.1.0 - 2016-08-28
------------------

- Initial release.

.. _Unreleased: https://github.com/Stranger6667/pyoffers/compare/0.6.3...HEAD
.. _0.6.3: https://github.com/Stranger6667/pyoffers/compare/0.6.2...0.6.3
.. _0.6.2: https://github.com/Stranger6667/pyoffers/compare/0.6.1...0.6.2
.. _0.6.1: https://github.com/Stranger6667/pyoffers/compare/0.6.0...0.6.1
.. _0.6.0: https://github.com/Stranger6667/pyoffers/compare/0.5.0...0.6.0
.. _0.5.0: https://github.com/Stranger6667/pyoffers/compare/0.4.4...0.5.0
.. _0.4.4: https://github.com/Stranger6667/pyoffers/compare/0.4.3...0.4.4
.. _0.4.3: https://github.com/Stranger6667/pyoffers/compare/0.4.2...0.4.3
.. _0.4.2: https://github.com/Stranger6667/pyoffers/compare/0.4.1...0.4.2
.. _0.4.1: https://github.com/Stranger6667/pyoffers/compare/0.4.0...0.4.1
.. _0.4.0: https://github.com/Stranger6667/pyoffers/compare/0.3.2...0.4.0
.. _0.3.2: https://github.com/Stranger6667/pyoffers/compare/0.3.1...0.3.2
.. _0.3.1: https://github.com/Stranger6667/pyoffers/compare/0.3.0...0.3.1
.. _0.3.0: https://github.com/Stranger6667/pyoffers/compare/0.2.2...0.3.0
.. _0.2.2: https://github.com/Stranger6667/pyoffers/compare/0.2.1...0.2.2
.. _0.2.1: https://github.com/Stranger6667/pyoffers/compare/0.2.0...0.2.1
.. _0.2.0: https://github.com/Stranger6667/pyoffers/compare/0.1.2...0.2.0
.. _0.1.2: https://github.com/Stranger6667/pyoffers/compare/0.1.1...0.1.2
.. _0.1.1: https://github.com/Stranger6667/pyoffers/compare/0.1.0...0.1.1

.. _#52: https://github.com/Stranger6667/pyoffers/issues/52
.. _#51: https://github.com/Stranger6667/pyoffers/issues/51
.. _#48: https://github.com/Stranger6667/pyoffers/issues/48
.. _#45: https://github.com/Stranger6667/pyoffers/issues/45
.. _#43: https://github.com/Stranger6667/pyoffers/issues/43
.. _#42: https://github.com/Stranger6667/pyoffers/issues/42
.. _#41: https://github.com/Stranger6667/pyoffers/issues/41
.. _#40: https://github.com/Stranger6667/pyoffers/issues/40
.. _#39: https://github.com/Stranger6667/pyoffers/issues/39
.. _#38: https://github.com/Stranger6667/pyoffers/issues/38
.. _#36: https://github.com/Stranger6667/pyoffers/issues/36
.. _#35: https://github.com/Stranger6667/pyoffers/issues/35
.. _#34: https://github.com/Stranger6667/pyoffers/issues/34
.. _#33: https://github.com/Stranger6667/pyoffers/issues/33
.. _#32: https://github.com/Stranger6667/pyoffers/issues/32
.. _#31: https://github.com/Stranger6667/pyoffers/issues/31
.. _#29: https://github.com/Stranger6667/pyoffers/issues/29
.. _#28: https://github.com/Stranger6667/pyoffers/issues/28
.. _#27: https://github.com/Stranger6667/pyoffers/issues/27
.. _#26: https://github.com/Stranger6667/pyoffers/issues/26
.. _#25: https://github.com/Stranger6667/pyoffers/issues/25
.. _#24: https://github.com/Stranger6667/pyoffers/issues/24
.. _#23: https://github.com/Stranger6667/pyoffers/issues/23
.. _#22: https://github.com/Stranger6667/pyoffers/issues/22
.. _#21: https://github.com/Stranger6667/pyoffers/issues/21
.. _#20: https://github.com/Stranger6667/pyoffers/issues/20
.. _#19: https://github.com/Stranger6667/pyoffers/issues/19
.. _#18: https://github.com/Stranger6667/pyoffers/issues/18
.. _#17: https://github.com/Stranger6667/pyoffers/issues/17
.. _#16: https://github.com/Stranger6667/pyoffers/issues/16
.. _#14: https://github.com/Stranger6667/pyoffers/issues/14
.. _#13: https://github.com/Stranger6667/pyoffers/issues/13
.. _#12: https://github.com/Stranger6667/pyoffers/issues/12
.. _#11: https://github.com/Stranger6667/pyoffers/issues/11
.. _#10: https://github.com/Stranger6667/pyoffers/issues/10
.. _#9: https://github.com/Stranger6667/pyoffers/issues/9
.. _#8: https://github.com/Stranger6667/pyoffers/issues/8
.. _#7: https://github.com/Stranger6667/pyoffers/issues/7
.. _#6: https://github.com/Stranger6667/pyoffers/issues/6
.. _#5: https://github.com/Stranger6667/pyoffers/issues/5
.. _#3: https://github.com/Stranger6667/pyoffers/issues/3

.. _Stranger6667: https://github.com/Stranger6667
.. _iamanikeev: https://github.com/iamanikeev
