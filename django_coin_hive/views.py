# -*- coding: utf-8 -*-
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from django.db.models import Max, Sum, Avg
import json
from datetime import timedelta, datetime

from .models import CoinHiveUser, CoinHiveSite, CoinHiveCurrentHashRate


def get_site_hash_rate(site_key):
    SAMPLE_TIME_SIZE = 30
    cutoff = datetime.now() - timedelta(seconds=SAMPLE_TIME_SIZE)
    return CoinHiveCurrentHashRate.objects.filter(
        site__site_key=site_key,
        modified__gte=cutoff,
    ).aggregate(
        max=Max('hash_rate'),
        avg=Avg('hash_rate'),
        total=Sum('hash_rate'),
    )


def mine(request, site_name=None):
    template_name = "django_coin_hive/mine.html"
    context = {}
    if site_name:
        try:
            site = CoinHiveSite.objects.get(site_name=site_name)
        except CoinHiveSite.DoesNotExist:
            return HttpResponseBadRequest("Invalid site name provided")
    else:
        try:
            site = CoinHiveSite.objects.get(default=True)
        except CoinHiveSite.DoesNotExist:
            raise Exception("There needs to be a default Site")

    context.update({'site_key': site.site_key,})

    user = request.user
    if not isinstance(user, AnonymousUser):
        if user.coinhiveuser_set.count():
            coinhive_user = user.coinhiveuser_set.first()
        else:  # create one if one doesn't exist for the user
            coinhive_user = CoinHiveUser.objects.create(user=user)
        context.update({'coin_hive_user': coinhive_user.name})
    return render(request, template_name, context=context)


@csrf_exempt
def hash_rate(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            user_name = data.get('user')
            hash_rate = float(data.get('hash_rate'))
            site_key = data.get('site_key')
        except (IndexError, ValueError,):
            return HttpResponseBadRequest()
        try:
            user = CoinHiveUser.objects.get(name=user_name)
        except CoinHiveUser.DoesNotExist:
            return HttpResponseBadRequest("User does not exist")
        try:
            site = CoinHiveSite.objects.get(site_key=site_key)
        except CoinHiveUser.DoesNotExist:
            return HttpResponseBadRequest("Site does not exist")

        CoinHiveCurrentHashRate.objects.update_or_create(
            user=user,
            site=site,
            defaults={'hash_rate':hash_rate,},
        )

        stats = cache.get_or_set(
            site_key,
            lambda : get_site_hash_rate(site_key),
            10
        )
        return JsonResponse(stats)

    else:
        return HttpResponseNotAllowed(('GET', 'POST',))
