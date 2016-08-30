0.3.1.dev
=========

* Added `find_all` methods for all defined models. (`#23`_)
* Initial support for `contain` in `find_all` queries. (`#22`_)

0.3.0
=====

* Fixed invalid queries building. (`#16`_)
* Fixed error on empty not paginated results. (`#17`_)
* Fixed error on single result in `find_all` call. (`#18`_)
* Filters implementation. (`#6`_)

0.2.2
=====

* Fixed error on not paginated results. (`#14`_)

0.2.1
=====

* Don't touch cassette if it contains no production credentials. (`#12`_)
* Fixed exception if no results were found. (`#13`_)

0.2.0
=====

* Added support for returning multiple objects. (`#7`_)
* Refactored models instantiation. (`#9`_)
* Added `Conversion` model. (`#3`_)
* Better models representation. (`#8`_)
* Fixed credentials leak. (`#11`_)

0.1.2
=====

* Fixed query building for lists and tuples. (`#5`_)

0.1.1
=====

* Fixed packaging issue.

0.1.0
=====

* Initial release.


.. _#23: https://github.com/Stranger6667/pyoffers/issues/23
.. _#22: https://github.com/Stranger6667/pyoffers/issues/22
.. _#18: https://github.com/Stranger6667/pyoffers/issues/18
.. _#17: https://github.com/Stranger6667/pyoffers/issues/17
.. _#16: https://github.com/Stranger6667/pyoffers/issues/16
.. _#14: https://github.com/Stranger6667/pyoffers/issues/14
.. _#13: https://github.com/Stranger6667/pyoffers/issues/13
.. _#12: https://github.com/Stranger6667/pyoffers/issues/12
.. _#11: https://github.com/Stranger6667/pyoffers/issues/11
.. _#9: https://github.com/Stranger6667/pyoffers/issues/9
.. _#8: https://github.com/Stranger6667/pyoffers/issues/8
.. _#7: https://github.com/Stranger6667/pyoffers/issues/7
.. _#6: https://github.com/Stranger6667/pyoffers/issues/6
.. _#5: https://github.com/Stranger6667/pyoffers/issues/5
.. _#3: https://github.com/Stranger6667/pyoffers/issues/3