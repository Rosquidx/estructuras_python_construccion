from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.cargar_index, name="index"),
    path('tuplas/', views.cargar_tuplas, name="tuplas"),
    path('dataclases/', views.cargar_dataclases, name="dataclases"),
    path('dictionaries/', views.cargar_dictionaries, name="dictionaries"),
    path('lists/', views.cargar_lists, name="lists"),
    path('sets/', views.cargar_sets, name="sets"),
    path('queues/', views.cargar_queues, name="queues"),
]
