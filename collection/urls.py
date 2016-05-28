from django.conf.urls import url
from django.contrib import admin
from .views import create, detail, update, delete


urlpatterns = [
    url(r'^create/$', create),
    url(r'^detail/$', detail),
    url(r'^update/$', update),
    url(r'^delete/$', delete),
]
