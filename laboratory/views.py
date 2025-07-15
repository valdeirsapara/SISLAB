from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contrib.decorators import constance_required
from contrib.services import LaboratoryService
from .models import Laboratory
from .forms import LaboratoryForm
from django.contrib import messages

@login_required
@constance_required('ALUGEL_LABORATORIO')
def index(request):
    """Lista todos os laboratórios ativos."""
    laboratorios = LaboratoryService.get_active_laboratories()

    context = {
        'laboratorios': laboratorios,
    }

    return render(request, 'laboratory/index.html', context=context)

@login_required
def add_laboratory(request):
    """Criar um novo laboratório."""
    if request.method == 'POST':
        form = LaboratoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Laboratório criado com sucesso!")
            return redirect(reverse('laboratory_index'))
        else:
            messages.error(request, "Erro ao criar laboratório. Verifique os dados informados.")
    else:
        form = LaboratoryForm()
    
    return render(request, 'laboratory/add.html', {
        'form': form,
        'title': 'Adicionar Laboratório'
    })

@login_required 
def edit_laboratory(request, id):
    """Editar um laboratório existente."""
    laboratory = get_object_or_404(Laboratory, id=id)
    
    if request.method == 'POST':
        form = LaboratoryForm(request.POST, instance=laboratory)
        if form.is_valid():
            form.save()
            messages.success(request, "Laboratório atualizado com sucesso!")
            return redirect(reverse('laboratory_index'))
        else:
            messages.error(request, "Erro ao atualizar laboratório. Verifique os dados informados.")
    else:
        form = LaboratoryForm(instance=laboratory)
    
    return render(request, 'laboratory/add.html', {
        'form': form,
        'laboratory': laboratory,
        'title': 'Editar Laboratório'
    })