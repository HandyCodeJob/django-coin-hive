# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
	regex=r'^miner?/?$',
	view=views.CoinHiveMineView.as_view(),
	name='mine',
    ),
]