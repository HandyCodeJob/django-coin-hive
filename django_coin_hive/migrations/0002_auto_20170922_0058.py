# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-22 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_coin_hive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinhiveuser',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
