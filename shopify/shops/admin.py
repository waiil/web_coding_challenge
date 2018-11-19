# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import DislikedShop, Shop

# Register your models here.

admin.site.register(DislikedShop,admin.ModelAdmin)
admin.site.register(Shop,admin.ModelAdmin)