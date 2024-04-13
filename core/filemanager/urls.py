from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('filemanager/', views.home, name='filemanager'),
    path('filemanager/get', views.get, name='get'),
    path('filemanager/add', views.add, name='add'),
    path('filemanager/edit', views.edit, name='edit'),
    path('filemanager/delete', views.delete, name='delete'),
    path('filemanager/search', views.search, name='search'),
]
