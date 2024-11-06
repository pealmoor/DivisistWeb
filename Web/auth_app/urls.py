from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('logout', LogoutView.as_view()) 
]