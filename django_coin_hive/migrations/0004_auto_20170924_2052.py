# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_coin_hive', '0003_auto_20170924_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinHiveCurrentHashRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hash_rate', models.FloatField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_coin_hive.CoinHiveSite')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_coin_hive.CoinHiveUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='coinhiveevent',
            name='user',
        ),
        migrations.DeleteModel(
            name='CoinHiveEvent',
        ),
    ]