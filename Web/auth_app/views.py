from django.shortcuts import render
import logging

# Create your views here.
def login_view(request):
    return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, '/Web/templates/index.html')

def google_callback(request):
    """
    Maneja el callback después del inicio de sesión con Google.
    """
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Aquí puedes procesar los datos del usuario, si es necesario
        try:
            social_account = SocialAccount.objects.get(user=request.user)
            print(f"Usuario autenticado con Google: {social_account.extra_data}")
        except SocialAccount.DoesNotExist:
            pass

        # Redirige a la página deseada
        return redirect("http://127.0.0.1:5500/DivisistWeb/Web/templates/index.html")  # Cambia por la URL deseada
    else:
        # Si no está autenticado, redirige al login
        return redirect('/auth/google/login/')    



logger = logging.getLogger(__name__)

def google_callback(request):
    logger.info(f"Callback recibido para el usuario: {request.user}")
    # El resto de tu lógica
