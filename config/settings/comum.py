# standard
from collections import OrderedDict
import json
import os
from decouple import config

# django
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY',default='django-insecure-&#o)8(q5ajrd5(@wn2j+*uy-ie92j)oia*in=3t3+i=-1$s8a1')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')


# Application definition

INSTALLED_APPS = [
    'constance',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

INSTALLED_APPS += [
    'contrib',
    'laboratory',
    'news',
    'perfil',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data' / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = config('TIME_ZONE', default='UCT')

USE_I18N = True

USE_TZ = True


MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles_producao'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




#
# Constance Backends
#
CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_REDIS_CONNECTION = {
    'host': config('REDIS_HOST', default='localhost'),
    'port': config('REDIS_PORT', default=6379, cast=int),
    'db': 0,
}


JSON_CONFIGS = []
with open('config/config.json','r', encoding='utf-8') as f:
    JSON_CONFIGS = json.load(f)

CONSTANCE_CONFIG = OrderedDict()
CONSTANCE_ADDITIONAL_FIELDS = {}
CONSTANCE_CONFIG_FIELDSETS = OrderedDict()
type_mapping = {
        'number': int,
        'bool': bool,
        'float': float,
        'text': str,
    }
    

for section in JSON_CONFIGS:
    fieldset_fields = []
    
    for argument in section['arguments']:
        if argument.get('readonly', False):
            continue
        default = argument.get('default', "")
        fieldset_fields.append(argument['name'])
        if argument['type'] == 'select':
            CONSTANCE_ADDITIONAL_FIELDS[argument['name']] = [
                'django.forms.fields.ChoiceField',
                {
                    'widget': 'django.forms.Select',
                    'choices': tuple(argument['options'].items())
                }
            ]
            CONSTANCE_CONFIG.update([(argument['name'], (default, argument['label'], argument['name']))])
        else:
            CONSTANCE_CONFIG.update({argument['name']: (default, argument['label'], type_mapping.get(argument['type'],str))})
    
    CONSTANCE_CONFIG_FIELDSETS[section['name']] = {
        'fields': tuple(fieldset_fields),
        'collapse': False
    }



CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS',default='https://localhost:8000;http://localhost:8000',).split(';')