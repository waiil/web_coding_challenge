# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Shop(models.Model):
    google_id = models.CharField(verbose_name=_('Google ID'), max_length=255)
    name = models.CharField(verbose_name=_(u'Shop name'), max_length=255)
    rating = models.FloatField(verbose_name=_('Rating'))
    address = models.CharField(verbose_name=_('Shop Address'), max_length=255)
    longitude = models.FloatField(verbose_name=_(u'longitude'))
    latitude = models.FloatField(verbose_name=_(u'Latitude'))
    # TO DO : UPDATE TO ARRAY FIELD
    favoris_of = models.CharField(blank=True, null=True, verbose_name=_(u'Favoris of'), max_length=255)

    def __unicode__(self):
        return "%s %s" % (self.longitude, self.latitude)