from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('page_show', views.page_show, name="page_show"),
    path('textAdd', views.textAdd, name="textAdd")

]