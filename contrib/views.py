from django.shortcuts import render
from contrib.models import Laboratorio, Noticia, Model3D, Livro

# Create your views here.
def home(request):
    laboratorios = Laboratorio.objects.filter(ativo=True,status=Laboratorio.DISPONIVEL)
    noticia = Noticia.objects.latest('data_modificacao')
    modelo3d = Model3D.objects.latest('data_modificacao')
    livro = Livro.objects.latest('data_modificacao')
    return render(request, 'home.html', locals())