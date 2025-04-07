from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contrib.decorators import constance_required
from .models import Laboratory
from django.contrib import messages

@login_required
@constance_required('ALUGEL_LABORATORIO')
def index(request):
    

    laboratorios = Laboratory.objects.filter(ativo=True,)

    _context = {
        'laboratorios': laboratorios,
    }

    return render(request, 'laboratory/index.html', context=_context)

@login_required
def add_laboratory(request, id=None):
    if request.method == 'POST':
        if id:
            laboratory = Laboratory.objects.get(id=id)
        else:
            laboratory = Laboratory.objects.create(nome= request.POST.get('nome'))

        laboratory.nome = request.POST.get('nome')
        laboratory.status = int(request.POST.get('status'))
        laboratory.save()
        messages.success(request, "Laboratório salvo com sucesso!")
        return redirect(reverse('laboratory_index'))

    if id:
        laboratory = Laboratory.objects.get(id=id)
    else:
        laboratory = None
    return render(request, 'laboratory/add.html', context={
        'laboratory': laboratory,
    })