from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'auth_app/login.html')

def index(request):
    return render(request, 'index.html')