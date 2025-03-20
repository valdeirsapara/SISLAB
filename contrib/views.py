from django.shortcuts import render

from contrib.models import Model3D, Livro
from laboratory.models import Laboratory
from news.models import News

# Create your views here.
def home(request):
    laboratories = Laboratory.objects.filter(ativo=True,status=Laboratory.DISPONIVEL)
    news = News.objects.filter(ativo=True).order_by('-data_criacao').first()
    modelo3d = Model3D.objects.filter(ativo=True).order_by('data_modificacao').first()
    livro = Livro.objects.filter(ativo=True).order_by('data_modificacao').first()
    return render(request, 'home.html', locals())