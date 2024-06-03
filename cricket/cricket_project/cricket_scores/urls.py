# cricket_scores/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('live/', views.live_matches, name='live_matches'),
]
