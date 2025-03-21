from .comum import *


TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa: F405
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='sislab_db'),
        'USER': config('DB_USER', default='sislab_user'),
        'PASSWORD': config('DB_PASSWORD',),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default='5432'),
        'CONN_MAX_AGE': 600,  # Manter conexões por 10 minutos
    }
}