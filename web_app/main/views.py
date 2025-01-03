
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.index, name='register'),  # Используем основную страницу для регистрации
    path('login/', views.user_login, name='user_login')
]
