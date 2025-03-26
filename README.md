# SISLAB - Sistema de Gerenciamento de Recursos Laboratoriais

## Sobre o Projeto

SISLAB é um sistema desenvolvido para controlar o acesso e uso de recursos em laboratórios educacionais. Esta plataforma permite que professores e usuários autorizados possam agendar horários de uso do laboratório, emprestar livros e utilizar modelos 3D disponíveis.

O sistema possui um fluxo de aprovação onde as solicitações dos usuários precisam ser aceitas por um gerente.

## Tecnologias

- **Backend**: Django 5.1
- **Banco de Dados**: SQLite (para desenvolvimento) / PostgreSQL (para produção)
- **Cache**: Redis
- **Containerização**: Docker e Docker Compose

## Configuração com Docker

### 1. Pré-requisitos

- Docker
- Docker Compose

### 2. Configuração Inicial

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/SISLAB.git
cd SISLAB
```

2. **Configure o arquivo .env**

Copie o arquivo `.env.exemple` para `.env`:

```bash
cp .env.exemple .env
```

Edite o arquivo `.env` com suas configurações:

```
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TIME_ZONE=America/Boa_Vista
```

### 3. Configuração dos Arquivos Estáticos

> **IMPORTANTE**: O projeto utiliza uma estrutura modular de configurações com os seguintes arquivos:
> - `config/settings/comum.py` - Configurações compartilhadas entre todos os ambientes
> - `config/settings/dev.py` - Configurações específicas para desenvolvimento
> - `config/settings/prod.py` - Configurações específicas para produção

Certifique-se de que a configuração de arquivos estáticos no arquivo `config/settings/comum.py` esteja correta:

```python
# Diretório onde seus arquivos estáticos de desenvolvimento estão localizados
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Diretório para onde os arquivos estáticos serão coletados em produção
STATIC_ROOT = BASE_DIR / 'staticfiles_producao'

# URL para acessar os arquivos estáticos
STATIC_URL = '/static/'
```

Esta configuração evita o erro `STATICFILES_DIRS setting should not contain the STATIC_ROOT setting`.

### 4. Execução com Docker

#### Importante: Escolha o ambiente de execução

Decida se você quer executar o projeto em ambiente de desenvolvimento ou produção. 
O projeto vem com arquivos de configuração separados para cada ambiente.

#### Para desenvolvimento

**É crucial copiar o arquivo de override para desenvolvimento:**

```bash
# Copie o arquivo de configuração para desenvolvimento
cp docker/override/docker-compose.override.dev.yml docker-compose.override.yml

# Inicie os contêineres
docker-compose up -d
```

O arquivo `docker-compose.override.dev.yml` configura o ambiente de desenvolvimento com:
- Montagem de volumes para atualização em tempo real do código
- Porta 8000 exposta para acesso local
- Execução do servidor de desenvolvimento do Django

#### Para produção

Para configurar o ambiente de produção:

```bash
# Copie o arquivo de configuração para produção
cp docker/override/docker-compose.override.prod.yml docker-compose.override.yml

# Inicie os contêineres
docker-compose up -d
```

O arquivo `docker-compose.override.prod.yml` configura o ambiente de produção com:
- Banco de dados PostgreSQL
- Servidor web usando uWSGI
- Configuração otimizada para ambiente de produção
- Porta 80 exposta para acesso via navegador

### 5. Acesso à Aplicação

Após iniciar os contêineres:

```
# Ambiente de desenvolvimento:
http://localhost:8000

# Ambiente de produção:
http://localhost (ou http://localhost:80)
```

## Execução sem Docker (Desenvolvimento Local)

Caso prefira executar o sistema diretamente sem Docker, siga estas etapas:

### 1. Configure o ambiente

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements/local.txt
```

### 2. Configure o arquivo .env

```bash
cp .env.exemple .env
# Edite o arquivo .env conforme necessário
```

### 3. Configure o Redis

O projeto utiliza Redis para configurações dinâmicas via Constance. Você precisará:

```bash
# Instalar o servidor Redis
# No Ubuntu/Debian:
sudo apt install redis-server

# No macOS:
brew install redis

# No Windows:
# Baixe o Redis para Windows ou use o Docker apenas para Redis:
docker run --name redis -p 6379:6379 -d redis
```

### 4. Defina o ambiente de execução

```bash
# No Windows:
set DJANGO_SETTINGS_MODULE=config.settings.dev

# No Linux/Mac:
export DJANGO_SETTINGS_MODULE=config.settings.dev
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse a aplicação em `http://127.0.0.1:8000`

## Estrutura Docker

O projeto utiliza múltiplos arquivos Docker para separar preocupações:

- `docker-compose.yml` - Definição principal dos serviços
- `docker/python/Dockerfile` - Imagem base com Python e dependências
- `docker/web/Dockerfile` - Imagem para o serviço web
- `docker/override/docker-compose.override.dev.yml` - Configurações específicas para desenvolvimento
- `docker/override/docker-compose.override.prod.yml` - Configurações específicas para produção

## Comandos Docker Úteis

```bash
# Iniciar os contêineres
docker-compose up -d

# Parar os contêineres
docker-compose down

# Ver logs
docker-compose logs -f

# Executar comandos Django
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# Reconstruir imagens
docker-compose build

# Verificar status dos contêineres
docker-compose ps

# Limpar volumes (cuidado: isso apaga dados)
docker-compose down -v
```

## Ambientes de Execução

O SISLAB está configurado para funcionar em diferentes ambientes através de múltiplos arquivos de configuração:

### Configuração de Ambientes

A aplicação utiliza três arquivos principais para configuração:

- `config/settings/comum.py` - Configurações compartilhadas por todos os ambientes
- `config/settings/dev.py` - Configurações específicas para desenvolvimento
- `config/settings/prod.py` - Configurações específicas para produção

O ambiente é determinado pela variável de ambiente `DJANGO_SETTINGS_MODULE`:
- Para desenvolvimento: `config.settings.dev`
- Para produção: `config.settings.prod`

### Ambiente de Desenvolvimento
- Usa SQLite como banco de dados
- Recarregamento automático de código
- Debug ativado
- Ideal para desenvolvimento diário
- Definido em `config/settings/dev.py`

### Ambiente de Produção
- Usa PostgreSQL como banco de dados
- Servidor uWSGI otimizado
- Arquivos estáticos servidos eficientemente
- Cache Redis configurado
- Debug desativado
- Definido em `config/settings/prod.py`

## Solução de Problemas

### Erro com Arquivos Estáticos

Se você encontrar o erro:
```
SystemCheckError: System check identified some issues:
ERRORS:
?: (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
```

Verifique se:
1. `STATIC_ROOT` e `STATICFILES_DIRS` apontam para diretórios diferentes
2. Os diretórios necessários existem
3. O Dockerfile está executando corretamente o comando `collectstatic`

### Erro de Permissão com Docker

Se encontrar esse erro:
```
 > [web internal] load build context:
------
failed to solve: error from sender: open /home/valdeir/projetos/sislab/data/postgres/base/1: permission denied
```

use o comando:
`sudo setfacl -R -d -m u::rwx,g::rwx,o::rwx {caminho da raiz}/data`

ou
`sudo chmod -R 777 /home/valdeir/projetos/sislab/data`

### Problemas com o Redis

Se você tiver problemas com a conexão ao Redis:

1. Verifique se o serviço está rodando:
```bash
docker-compose ps redis
```

2. Teste a conexão manualmente:
```bash
docker-compose exec redis redis-cli ping
```

Deve retornar "PONG" se estiver funcionando corretamente.

## Acessando o Sistema

### Criando um Superusuário

Para acessar o painel administrativo:

```bash
# No modo Docker
docker-compose exec web python manage.py createsuperuser

# Sem Docker
python manage.py createsuperuser
```

Siga as instruções para criar um usuário administrativo.

### Login

O sistema suporta login tanto por nome de usuário quanto por email. 
Acesse a página de login em `/login/` e use as credenciais criadas.