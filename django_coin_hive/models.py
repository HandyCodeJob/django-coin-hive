# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


from model_utils.models import TimeStampedModel


class CoinHiveUser(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    balance = models.IntegerField()

    def __str__(self):
        return f"{user}, {balance} hashes"
    

class CoinHiveToken(TimeStampedModel):
    user = models.ForeignKey(
        'CoinHiveUser',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    token = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    target = models.IntegerField()
    hashes = models.IntegerField()

    def __str__(self):
        return f"{token}, {target}/{hashes}"
