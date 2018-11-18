from django.conf.urls import url
from .views import home, like_shop, dislike_shop


urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^like-shop/', like_shop, name="like_shop"),
    url(r'^dislike-shop/', dislike_shop, name="dislike_shop"),
]