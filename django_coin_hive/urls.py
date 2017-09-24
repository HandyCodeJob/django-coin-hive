# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
	regex=r'^miner/(?P<site_name>\w+)?',
	view=views.mine,
	name='miner',
    ),
    url(
        regex=r'^hash_rate/$',
        view=views.hash_rate,
        name='hash-rate',
    ),
]
