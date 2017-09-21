=====
Usage
=====

To use Django Coin-Hive in a project, add it to your `INSTALLED_APPS`:

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
