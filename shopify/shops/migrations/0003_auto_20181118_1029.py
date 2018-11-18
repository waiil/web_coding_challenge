# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20181117_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default='test address', max_length=255, verbose_name='Shop Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='favoris_of',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Favoris of'),
        ),
        migrations.AddField(
            model_name='shop',
            name='google_id',
            field=models.CharField(default='321sdfsd', max_length=255, verbose_name='Google ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='name',
            field=models.CharField(default='test name', max_length=255, verbose_name='Shop name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='rating',
            field=models.FloatField(default=2, verbose_name='Rating'),
            preserve_default=False,
        ),
    ]
