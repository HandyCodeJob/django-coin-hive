# -*- coding: utf-8 -*-
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.core.cache import cache
from django.db.models import Max, Sum

from .models import CoinHiveUser


def get_stats(tag):
    return CoinHiveEvent.objects.filter(tag=tag).annotate(
        sum=F('hashes') / F('interval')
    ).aggregate(
        max=Max('sum'),
        avg=Avg('sum'),
        total=Sum('sum'),
    )


class CoinHiveMineView(TemplateView):
    template_name = "django_coin_hive/mine.html"

    def get_context_data(self, **kwargs):
        context = {
            'site_key': settings.COIN_HIVE_SITE_KEY,
        }
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            if user.coinhiveuser_set.count():
                coinhive_user = user.coinhiveuser_set.first()
            else:  # create one if one doesn't exist for the user
                coinhive_user = CoinHiveUser.objects.create(user=user)

            context.update({'coin_hive_user': coinhive_user.name})
        return context


def report(request):
    STATS_INTERVAL
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            coin_hive_user = request.POST.get('coin_hive_user', '')
            time_live = request.POST.get('time_live')
            interval = request.POST.get('interval')
            accepted_hashes = int(request.POST.get('accepted_hashes'))
            tag = request.POST.get('tag', '')
        except (IndexError, ValueError,):
            return HttpResponseBadRequest()
        try:
            user = CoinHiveUser.objects.get(name=coin_hive_user)
        except CoinHiveUser.DoesNotExist:
            return HttpResponseBadRequest()
        CoinHiveEvent.objects.create(
            user=user,
            interval=interval,
            time_live=time_live,
            hashes=accepted_hashes,
            tag=tag,
        )
        return JsonResponse({'success': True})
        # return cache.get_or_set(tag, get_stats, STATS_INTERVAL)

    else:
        return HttpResponseNotAllowed(('GET', 'POST',))
