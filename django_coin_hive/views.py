# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.conf import settings


class CoinHiveMineView(TemplateView):
    template_name = "django_coin_hive/mine.html"

    def get_context_data(self, **kwargs):
        context = {'SITE_KEY': settings.COIN_HIVE_SITE_KEY}
        return context
