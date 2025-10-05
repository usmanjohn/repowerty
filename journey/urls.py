from django.urls import path
from . import views

urlpatterns = [
    path('', views.journey_home, name = 'journey-home')
]