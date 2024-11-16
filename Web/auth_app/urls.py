from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout', LogoutView.as_view()),
    path('', views.index, name='index'), 
]