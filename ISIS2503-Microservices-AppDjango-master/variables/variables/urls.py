from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r'^variables/', views.VariableList, name='variableList'),
    url(r'^variablecreate/$', csrf_exempt(views.VariableCreate), name='variableCreate'),
]