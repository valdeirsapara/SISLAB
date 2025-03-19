from django.shortcuts import render
from contrib.models import Laboratorio

# Create your views here.
def home(request):
    laboratorios = Laboratorio.objects.filter(ativo=True)
    return render(request, 'home.html', {'laboratorios': laboratorios})