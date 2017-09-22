# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.conf import settings

from .models import CoinHiveUser


class CoinHiveMineView(TemplateView):
    template_name = "django_coin_hive/mine.html"

    def get_context_data(self, **kwargs):
        context = {'SITE_KEY': settings.COIN_HIVE_SITE_KEY}
        return context

class CoinHiveUserView(TemplateView):
    template_name = "django_coin_hive/user.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.coinhiveuser_set.count():
            coinhive_user = user.coinhiveuser_set.first()
        else:
            coinhive_user = CoinHiveUser.objects.create(user=user)
        
        context = {
            'SITE_KEY': settings.COIN_HIVE_SITE_KEY,
            'coinHiveUserName': coinhive_user.name,
        }
        return context

