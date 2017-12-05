# alexishomepage/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^resume/$', views.resume),
    url(r'^headshots/$', views.headshots),
    url(r'^reel/$', views.reel),
    url(r'^media/$', views.media),
    url(r'^contact/$', views.contact),
]
