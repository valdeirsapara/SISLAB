from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    next = request.GET.get('next', '/')
    print(next)

    if request.method == 'POST':
        data = request.POST
        next = data.get('next','/')
        user:User = authenticate(request, username=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            print(user)
            if next:
                return redirect(next)
            return redirect('/')
            
        else:
            messages.error(request, "Email ou senha incorretos, por favor tente novamente")
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('/') 