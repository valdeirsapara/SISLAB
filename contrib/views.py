from django.shortcuts import render
from contrib.models import Model3D, Livro
from contrib.services import LaboratoryService
from news.models import News


def home(request):
    """View principal da aplicação."""
    # Usar o serviço para obter laboratórios disponíveis
    laboratories = LaboratoryService.get_available_laboratories()[:3]
    
    # Obter outras informações para a home
    news = News.objects.filter(ativo=True).order_by('-data_criacao').first()
    modelo3d = Model3D.objects.filter(ativo=True).order_by('data_modificacao').first()
    livro = Livro.objects.filter(ativo=True).order_by('data_modificacao').first()
    
    context = {
        'laboratories': laboratories,
        'news': news,
        'modelo3d': modelo3d,
        'livro': livro
    }
    
    return render(request, 'home.html', context)