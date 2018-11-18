# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import googlemaps
from django.conf import settings
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.contrib.auth.decorators import login_required
from .utils import get_public_ip, get_location, save_shops
from .models import Shop, DislikedShop
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
        address=place['vicinity'],
        icon = place['icon']

    ) for place in places['results']]
    threading.Thread(target=save_shops, args=shops).start()
    return render(request, template_name='index.html', status=200, context={'shops': shops})
    # return JsonResponse({'places':places,"ip":request.session['ip'], 'location': request.session['location']})


@login_required(login_url="accounts/login")
def like_shop(request):
    google_shop_id = request.GET.get('id', None)
    if not google_shop_id:
        return JsonResponse({"success": False, "message": "id required!"}, status=HTTP_400_BAD_REQUEST)
    liked_shop = Shop.objects.filter(google_id=google_shop_id).first()
    if not liked_shop:
        return JsonResponse({"success": False, "message": "shop not found!"}, status=HTTP_404_NOT_FOUND)
    liked_shop.favoris_of = request.user.username
    liked_shop.save()
    return JsonResponse({"success": True, "message": "shop added to your favoris"}, status=HTTP_200_OK)


@login_required(login_url="accounts/login")
def dislike_shop(request):
    google_shop_id = request.GET.get('id', None)
    if not google_shop_id:
        return JsonResponse({"success": False, "message": "id required!"}, status=HTTP_400_BAD_REQUEST)
    shop = Shop.objects.filter(google_id=google_shop_id).first()
    if not shop:
        return JsonResponse({"success": False, "message": "shop not found!"}, status=HTTP_404_NOT_FOUND)
    disliked_shop = DislikedShop.objects.filter(user=request.user.username, shop=shop)
    if not disliked_shop:
        disliked_shop = DislikedShop.objects.create(shop=shop, user=request.user.username)
    disliked_shop.save()
    return JsonResponse({"success": True, "message": "shop successfully removed from nearby shops"}, status=HTTP_200_OK)
