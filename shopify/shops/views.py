# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import googlemaps
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .utils import get_public_ip, get_location, save_shops
from .models import Shop
import threading
from django.shortcuts import render
import json

# Create your views here.


@login_required(login_url="accounts/login")
def home(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    if 'location' not in request.session:
        ip = request.META.get('REMOTE_ADDR', None)
        if '127.0' in ip or ip == 'localhost':
            ip = get_public_ip()
        location = get_location(ip)
        request.session['location'] = location
        request.session['ip'] = ip
    places = gmaps.places_nearby(
        location=(request.session['location']['latitude'], request.session['location']['longitude']),
        rank_by="distance",
        keyword='shop'
    )
    shops = [Shop(
        name=place['name'],
        rating=place['rating'],
        latitude=place['geometry']['location']['lat'],
        longitude=place['geometry']['location']['lng'],
        google_id=place['place_id'],
        address=place['vicinity']

    ) for place in places['results']]
    threading.Thread(target=save_shops, args=shops).start()
    return render(request, template_name='index.html', status=200)
    # return JsonResponse({'places':places,"ip":request.session['ip'], 'location': request.session['location']})
