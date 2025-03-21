from .comum import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='sislab_db'),
        'USER': config('DB_USER', default='sislab_user'),
        'PASSWORD': config('DB_PASSWORD', default='sua_senha_segura'),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default='5432'),
        'CONN_MAX_AGE': 600,  # Manter conexões por 10 minutos
        'OPTIONS': {
            'connect_timeout': 10,
            'client_encoding': 'UTF8',
            'timezone': 'UTC',
            # Configurações para otimização de desempenho
            'sslmode': 'prefer',  # Use 'require' em ambientes públicos
            'application_name': 'sislab',
            'keepalives': 1,
            'keepalives_idle': 30,
            'keepalives_interval': 10,
            'keepalives_count': 5,
        },
        'ATOMIC_REQUESTS': False,  # Não envolva cada solicitação em uma transação
        'AUTOCOMMIT': True,  # Autocommit habilitado
        # Configure o pool de conexões se estiver utilizando Django >= 4.1
        'POOL_OPTIONS': {
            'POOL_SIZE': 20,  # Número máximo de conexões no pool
            'MAX_OVERFLOW': 10,  # Número extra de conexões permitidas
            'RECYCLE': 300,  # Tempo em segundos para reciclar conexões
        },
    }
}