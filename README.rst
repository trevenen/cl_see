python-craigslist
=================

A simple `Craigslist <http://www.craigslist.org>`__ motorbike specific wrapper.

Disclaimer
----------

* I don't work for or have any affiliation with Craigslist.
* This module was implemented for educational purposes. It should not be used for crawling or downloading data from Craigslist.

Installation
------------

::

    pip install python-craigslist

Classes
-------

Base class:

* ``CraigslistBase``

Subclasses:

* ``CraigslistForSale`` (craigslist.org > for sale)

Usage
-----

Every subclass has its own set of filters. To get a list of all the filters
supported by a specific subclass, use the ``.show_filters()`` class-method:
If you need a filter that doesn't exist, create it.

.. code:: python

   >>> from craigslist import CraigslistJobs, CraigslistForSale
   >>> CraigslistJobs.show_filters()

   Base filters:
   * posted_today = True/False
   * query = ...
   * search_titles = True/False
   * has_image = True/False
   Section specific filters:
   * is_internship = True/False
   * is_telecommuting = True/False
   * is_contract = True/False
   * is_parttime = True/False
   * is_nonprofit = True/False
   * employment_type = u'full-time', u'part-time', u'contract', u"employee's choice"

   >>> CraigslistForSale.show_filters(category='cta')

   Base filters:
   * posted_today = True/False
   * query = ...
   * search_titles = True/False
   * has_image = True/False
   Section specific filters:
   * min_year = ...
   * model = ...
   * min_price = ...
   * max_miles = ...
   * make = ...
   * max_price = ...
   * min_miles = ...
   * max_year = ...
   * auto_title_status = u'clean', u'salvage', u'rebuilt', u'parts only', u'lien', u'missing'
   * auto_transmission = u'manual', u'automatic', u'other'
   * auto_fuel_type = u'gas', u'diesel', u'hybrid', u'electric', u'other'
   * auto_paint = u'black', u'blue', u'brown', u'green', u'grey', u'orange', u'purple', u'red', u'silver', u'white', u'yellow', u'custom'
   * auto_bodytype = u'bus', u'convertible', u'coupe', u'hatchback', u'mini-van', u'offroad', u'pickup', u'sedan', u'truck', u'SUV', u'wagon', u'van', u'other'
   * auto_drivetrain = u'fwd', u'rwd', u'4wd'
   * auto_size = u'compact', u'full-size', u'mid-size', u'sub-compact'
   * auto_cylinders = u'3 cylinders', u'4 cylinders', u'5 cylinders', u'6 cylinders', u'8 cylinders', u'10 cylinders', u'12 cylinders', u'other'
   * condition = u'new', u'like new', u'excellent', u'good', u'fair', u'salvage'
 
