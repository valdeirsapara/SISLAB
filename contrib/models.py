from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    """Modelo para perfil estendido do usuário."""
    SEXO_CHOICE = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    )
    matricula = models.CharField(max_length=255, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICE)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_full_name() or self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class Model3D(models.Model):
    """Modelo para modelos 3D disponíveis no sistema."""
    
    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobre = models.TextField(verbose_name='Descrição')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_modificacao = models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')

    class Meta:
        verbose_name = 'Modelo 3D'
        verbose_name_plural = 'Modelos 3D'
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    """Modelo para livros disponíveis no sistema."""
    
    nome = models.CharField(max_length=255, verbose_name='Título')
    autor = models.CharField(max_length=255, verbose_name='Autor')
    editora = models.CharField(max_length=255, verbose_name='Editora')
    localizacao = models.CharField(max_length=255, verbose_name='Localização')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_modificacao = models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['nome']