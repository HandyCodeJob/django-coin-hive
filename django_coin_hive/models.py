# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.conf import settings


from model_utils.models import TimeStampedModel
from model_utils.fields import AutoCreatedField


class CoinHiveSite(TimeStampedModel):
    site_name = models.CharField(max_length=255)
    site_key = models.CharField(max_length=32)
    secret_key = models.CharField(max_length=32)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.site_name} - {self.site_key}"


class CoinHiveUser(TimeStampedModel):
    """
    While we use ForeignKeys to link users, having multiple CoinHiveUsers for
    each django user is not well suported. When looking for the CoinHiveUser,
    we use `.first()`. While a OneToOne relation might be a better fit, we
    choose to allow for multiple users be supported in the future.
    """
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


class CoinHiveToken(TimeStampedModel):
    user = models.ForeignKey(
        'CoinHiveUser',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    token = models.CharField(max_length=32)
    target = models.IntegerField()

    def __str__(self):
        return f"{self.token}, {self.target}/{self.hashes}"


class CoinHiveCurrentHashRate(TimeStampedModel):
    user = models.ForeignKey(
        'CoinHiveUser',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    site = models.ForeignKey(
        'CoinHiveSite',
        on_delete=models.CASCADE,
    )
    hash_rate = models.FloatField()
