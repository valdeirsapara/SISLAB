FROM python:3.13-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    netcat-traditional \
    python3-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Instalar dependências
RUN mkdir -p /app/src/requirements/
RUN pip install --upgrade pip
ADD requirements/ /app/src/requirements/

ARG requirements=production


RUN pip install -r /app/src/requirements/$requirements.txt