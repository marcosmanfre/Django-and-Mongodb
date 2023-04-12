from django.urls import path

from . import views
import pymongo

urlpatterns = [path('', views.index,name='index'),]

