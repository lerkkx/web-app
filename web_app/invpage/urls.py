from django.urls import path
from .views import *

urlpatterns = [
    path('', create_request, name='index'),
    path('track_requests/', track_requests, name='track_requests'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('owned_inventory/', owned_inv, name='owned_inv'),
    path('reports/', reports_view, name='reports'),
]
