from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='Anasayfa'),
    path('text', views.text, name='Text'),
    path('analiz', views.analiz, name='Analiz')
]