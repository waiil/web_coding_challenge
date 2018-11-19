from .models import Shop, DislikedShop
from urllib2 import urlopen
from django.conf import settings
from django.db import transaction
import json
from dateutil.relativedelta import relativedelta
from datetime import datetime
from constants import HIDE_TIME


@transaction.atomic
def save_shops(*shops):
    for shop in shops:
        if Shop.objects.filter(google_id=shop.google_id).count() == 0:
            shop.save()


@transaction.atomic
def shops_to_display(shops, user):
    hide_time = datetime.now() - relativedelta(seconds=HIDE_TIME)
    results = []
    for shop in shops:
        if Shop.objects.filter(google_id=shop.google_id, favoris_of__contains=[user]).count() == 0 and \
                not DislikedShop.objects.filter(shop__google_id=shop.google_id, user=user, date__gt=hide_time).exists():
            results.append(shop)
    return results


def get_location(ip):
    url_location = "http://api.ipstack.com/{0}?access_key={1}".format(ip,settings.IP_STACK_KEY)
    return json.loads(urlopen(url_location).read())


def get_public_ip():
    return urlopen('http://ip.42.pl/raw').read()