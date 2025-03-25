from django.urls import reverse
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from constance import config
from constance.admin import get_values



# Create your views here.
@login_required
def settings_view(request):
    config_schema = settings.JSON_CONFIGS

    if request.method == 'POST':
        for group in config_schema:
            for arg in group.get('arguments', []):
                config_name = arg['name']

                if arg['type'] == 'bool':
                    config_value = config_name in request.POST
                elif arg['type'] == 'number':
                    config_value = int(request.POST.get(config_name, 0))
                elif arg['type'] == 'select':
                    config_value = request.POST.get(config_name, '')
                else:
                    config_value = request.POST.get(config_name, '')

                setattr(config, config_name, config_value)
        messages.success(request, "Configurações atualizadas com sucesso!")
        return HttpResponseRedirect(reverse('perfil_settings'))
    
    current_values = get_values()

    for group in config_schema:
        for arg in group.get('arguments', []):
            arg_name = arg['name']
            for arg in group.get('arguments', []):
                arg['value'] = current_values[arg_name]
                if arg_name in current_values:
                    arg['value'] = current_values[arg_name]
                else:
                    arg['value'] = arg.get('default', '')
            
    return render(request, 'perfil/settings.html', {
        'config_schema': config_schema,
        'title':'Painel de Configurações'
    })