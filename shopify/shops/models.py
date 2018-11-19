# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.postgres.fields import ArrayField
from constants import MAX_LENGTH
# Create your models here.


class Shop(models.Model):
    google_id = models.CharField(verbose_name=_('Google ID'), max_length=255, unique=True)
    name = models.CharField(verbose_name=_(u'Shop name'), max_length=255)
    rating = models.FloatField(verbose_name=_('Rating'))
    address = models.CharField(verbose_name=_('Shop Address'), max_length=255)
    longitude = models.FloatField(verbose_name=_(u'longitude'))
    latitude = models.FloatField(verbose_name=_(u'Latitude'))
    favoris_of = ArrayField(models.CharField(blank=True, null=True, verbose_name=_(u'Favoris of'), max_length=255),
                            default=[])
    icon = models.CharField(blank=True, null=True, verbose_name=_(u'Shop Icon'), max_length=100)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.longitude, self.latitude)

    def get_name(self):
        name = self.name[:MAX_LENGTH]
        if self.name != name:
            name += '...'
        return name


class DislikedShop(models.Model):
    shop = models.ForeignKey(Shop, verbose_name=_(u'Shop'))
    user = models.CharField(verbose_name=_(u'User'), max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s %s" % (self.shop, self.user, self.date)