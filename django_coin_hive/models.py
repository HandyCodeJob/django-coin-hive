# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.conf import settings


from model_utils.models import TimeStampedModel


class CoinHiveUser(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}, {self.balance} hashes"
    

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
        return f"{self.token}, {self.target}/{self.hashes}"
