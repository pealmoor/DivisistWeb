from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView
from . import views
from .views import login_view, logout_view

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('google/login/', include('allauth.urls')),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]