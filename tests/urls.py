# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from django_coin_hive.urls import urlpatterns as django_coin_hive_urls

urlpatterns = [
    url(r'^', include(django_coin_hive_urls, namespace='django_coin_hive')),
    url(r'^admin/', include(admin.site.urls)),
]
