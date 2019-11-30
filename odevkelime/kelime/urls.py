from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('hesapla', views.hesapla, name="hesapla"),
    path('hakkinda', views.hakkinda, name="hakkinda"),
]