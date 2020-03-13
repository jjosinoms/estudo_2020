from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('novo_post', views.post_new, name="novo_post"),

    path('cadastro', views.cadastro_usuario, name='cadadstroUsuario'),

    path('resultado',views.verificaLogin, name="verificaLogin"),
]
