from .models import Shop
from urllib2 import urlopen
from django.conf import settings
from django.db import transaction
import json


@transaction.atomic
def save_shops(*shops):
    for shop in shops:
        if Shop.objects.filter(google_id=shop.google_id).count() == 0:
            shop.save()


def get_location(ip):
    url_location = "http://api.ipstack.com/{0}?access_key={1}".format(ip,settings.IP_STACK_KEY)
    return json.loads(urlopen(url_location).read())


def get_public_ip():
    return urlopen('http://ip.42.pl/raw').read()