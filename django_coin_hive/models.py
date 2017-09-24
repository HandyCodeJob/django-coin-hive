# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.conf import settings


from model_utils.models import TimeStampedModel
from model_utils.fields import AutoCreatedField


class CoinHiveUser(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
    )
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}, {self.balance} hashes"


class CoinHiveEvent(models.Model):
    created = AutoCreatedField()
    user = models.ForeignKey(
        'CoinHiveUser',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    interval = models.FloatField()
    time_live = models.FloatField()
    hashes = models.IntegerField()
    tag = models.CharField(
        max_length=255,
        db_index=True,
        null=True,
    )

    def _hash_rate(self):
        return self.hashes/self.interval
    hash_rate = property(_hash_rate)


class CoinHiveToken(TimeStampedModel):
    user = models.ForeignKey(
        'CoinHiveUser',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    token = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    target = models.IntegerField()
    hashes = models.IntegerField()

    def __str__(self):
        return f"{self.token}, {self.target}/{self.hashes}"
