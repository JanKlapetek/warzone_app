from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadout_list, name='loadout_list'),
]