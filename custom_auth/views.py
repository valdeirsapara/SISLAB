from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.db import transaction

from .forms import LoginForm, UserRegistrationForm, PerfilForm
from contrib.models import Perfil
from contrib.utils import unique_username

User = get_user_model()


def login_view(request):
    """View para login de usuários."""
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        next_url = request.POST.get('next', '/')
        
        # Use the email as username for authentication
        email = request.POST.get('username')  # LoginForm uses 'username' field for email
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect(next_url if next_url else '/')
        else:
            messages.error(request, "Email ou senha incorretos, por favor tente novamente")
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', {
        'form': form,
        'next': next_url
    })


def register_view(request):
    """View para registro de novos usuários."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        
        if user_form.is_valid() and perfil_form.is_valid():
            try:
                with transaction.atomic():
                    # Criar usuário
                    user = user_form.save(commit=False)
                    user.set_password(user_form.cleaned_data['password'])
                    user.username = unique_username(user)
                    user.save()
                    
                    # Criar perfil
                    perfil = perfil_form.save(commit=False)
                    perfil.user = user
                    perfil.save()
                    
                    # Login automático
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    
                    messages.success(request, "Conta criada com sucesso!")
                    return redirect(reverse('home'))
                    
            except Exception as e:
                messages.error(request, "Erro ao criar conta. Tente novamente.")
        else:
            messages.error(request, "Erro nos dados informados. Verifique e tente novamente.")
    else:
        user_form = UserRegistrationForm()
        perfil_form = PerfilForm()
    
    return render(request, "auth/register.html", {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


def logout_view(request):
    """View para logout de usuários."""
    logout(request)
    return redirect('/') 