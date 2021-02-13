from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('login', views.login, name="login"),
    path('map', views.map, name="map"),
    path('thumbnail', views.thumbnail, name="thumbnail"),
]