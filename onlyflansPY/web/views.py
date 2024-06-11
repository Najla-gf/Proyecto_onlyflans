from django.shortcuts import render
from .models import Flan
from .forms import ContactFormModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

# contacto 

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def login_view(request):
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Si la autenticación es exitosa, iniciar sesión y redirigir al dashboard
            login(request, user)
            return HttpResponseRedirect('/welcome')
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            error_message = 'Credenciales incorrectas. Por favor, intenta de nuevo.'
            return render(request, 'login.html', {'error_message': error_message})
    # Renderizar la plantilla 'login.html' sin mensaje de error
    return render(request, 'login.html')
