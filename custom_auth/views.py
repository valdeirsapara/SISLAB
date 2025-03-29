from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

User = get_user_model()

from contrib.models import Perfil
from contrib.utils import unique_username


# Create your views here.
def login_view(request):
    next = request.GET.get('next', '/')
    print(next)

    if request.method == 'POST':
        data = request.POST
        next = data.get('next','/')
        user = authenticate(request, username=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            print(user)
            if next:
                return redirect(next)
            return redirect('/')
            
        else:
            messages.error(request, "Email ou senha incorretos, por favor tente novamente")
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        data = request.POST
        if data.get('email'):
            user, created = User.objects.get_or_create(email=data.get('email'))
            perfil, _ = Perfil.objects.get_or_create(user=user)
            if created:

                user.set_password(data.get('password'))
                user.first_name = data.get('first_name')
                user.last_name = data.get('last_name')
                user.username= unique_username(user)
                user.save()
                date_str = data.get('data_nascimento')
                print(date_str)
                if date_str:
                    perfil.data_nascimento = datetime.strptime(date_str, '%Y-%m-%d').date()
                perfil.matricula = data.get('matricula')
                perfil.sexo = data.get('sexo')
                perfil.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'  
                login(request, user) 
                return redirect(reverse('home'))
            else:
                messages.error(request, "O email já está em uso. Tente novamente com outro email.")
    return render(request, "auth/register.html")

def logout_view(request):
    logout(request)
    return redirect('/') 