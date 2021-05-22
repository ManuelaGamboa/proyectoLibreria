from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('novedades', views.novedades, name='novedades'),
    path('colecciones', views.colecciones, name='colecciones'),
    path('promociones', views.promociones, name='promociones'),

]