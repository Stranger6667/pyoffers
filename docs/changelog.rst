.. _changelog:

Changelog
=========

0.4.3.dev (TBA)
---------------

- Added `as_dict` method to models. `#39`_
- Better interface for models. `#38`_

0.4.2 (2016-09-01)
------------------

- Added ``raw`` argument to ``HasOffersAPI._call``. `#36`_
- Implemented ``findAllIds`` method. `#35`_
- Made SSL certificate verification optional. `#33`_

0.4.1 (2016-09-01)
------------------

- Fixed ``contain`` behaviour. `#32`_
- Improved sorting. `#31`_

0.4.0 (2016-08-31)
------------------

- Fixed managers sharing between API instances. `#26`_
- Better interface for ``update`` method. `#28`_
- Improved ``contain``. Added ``contain`` support to ``find_by_id`` method. `#27`_
- Implemented generic methods. `#10`_
- Implemented ``OR`` queries. `#19`_
- Implemented ``sort`` in queries. `#29`_

0.3.2 (2016-08-30)
------------------

- Added ``Country`` model. `#24`_
- Added ``get_target_countries`` method to ``Offer`` model. `#25`_

0.3.1 (2016-08-30)
------------------

- Added ``find_all`` methods for all defined models. `#23`_
- Initial support for ``contain`` in ``find_all`` queries. `#22`_
- Improved logging. `#20`_, `#21`_

0.3.0 (2016-08-30)
------------------

- Fixed invalid queries building. `#16`_
- Fixed error on empty not paginated results. `#17`_
- Fixed error on single result in ``find_all`` call. `#18`_
- Filters implementation. `#6`_

0.2.2 (2016-08-29)
------------------

- Fixed error on not paginated results. `#14`_

0.2.1 (2016-08-29)
------------------

- Don't touch cassette if it contains no production credentials. `#12`_
- Fixed exception if no results were found. `#13`_

0.2.0 (2016-08-29)
------------------

- Added support for returning multiple objects. `#7`_
- Refactored models instantiation. `#9`_
- Added ``Conversion`` model. `#3`_
- Better models representation. `#8`_
- Fixed credentials leak. `#11`_

0.1.2 (2016-08-29)
------------------

- Fixed query building for lists and tuples. `#5`_

0.1.1 (2016-08-28)
------------------

- Fixed packaging issue.

0.1.0 (2016-08-28)
------------------

- Initial release.


.. _#39: https://github.com/Stranger6667/pyoffers/issues/39
.. _#38: https://github.com/Stranger6667/pyoffers/issues/38
.. _#36: https://github.com/Stranger6667/pyoffers/issues/36
.. _#35: https://github.com/Stranger6667/pyoffers/issues/35
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