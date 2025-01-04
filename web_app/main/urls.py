from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('about/', views.about, name='about'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/complete/', views.password_reset_complete, name='password_reset_complete'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
]