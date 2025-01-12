from django.urls import path
from .views import create_request, track_requests

urlpatterns = [
    path('', create_request, name='index'),
    path('track_requests/', track_requests, name='track_requests'),
]
