from constance import config
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def constance_required(setting_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if getattr(config, setting_name, False):
                return view_func(request, *args, **kwargs)
            
            messages.error(request, "A funcionalidade não está habilitada.")
            return redirect(reverse('home'))
        return _wrapped_view
    return decorator