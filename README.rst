=============================
Django Coin-Hive
=============================

.. image:: https://badge.fury.io/py/django-coin-hive.svg
    :target: https://badge.fury.io/py/django-coin-hive

.. image:: https://travis-ci.org/sydhenry/django-coin-hive.svg?branch=master
    :target: https://travis-ci.org/sydhenry/django-coin-hive

.. image:: https://codecov.io/gh/sydhenry/django-coin-hive/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sydhenry/django-coin-hive

Intergrate Coin-Hive cryptocurrency miner with django projects

NOTE: This project is being built in tandem with another project. If you try to
use this package, you will run into problems. When this is released to pip, it
will be stable


Disclaimer
----------

This project is not endorsed by or affiliated with coinhive.com in any way.


Documentation
-------------

The full documentation is at https://django-coin-hive.readthedocs.io.

Quickstart
----------

Install Django Coin-Hive::

    pip install django-coin-hive

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_coin_hive.apps.DjangoCoinHiveConfig',
        ...
    )

Add Django Coin-Hive's URL patterns:

.. code-block:: python

    from django_coin_hive import urls as django_coin_hive_urls


    urlpatterns = [
        ...
        url(r'^', include(django_coin_hive_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
