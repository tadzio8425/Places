from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^places/', views.PlaceList, name='placesList'),
    url(r'^placecreate/$', csrf_exempt(views.PlaceCreate), name='placeCreate'),
]