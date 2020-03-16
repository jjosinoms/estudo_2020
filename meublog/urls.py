from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('novo_post', views.post_new, name="novo_post"),

]
