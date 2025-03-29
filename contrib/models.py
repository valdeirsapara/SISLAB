from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    SEXO_CHOICE = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    )
    matricula = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    data_nascimento = models.DateField( null=True)
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICE)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.user.username:  # Gera um username único baseado no nome
            self.user.username = f'{self.user.first_name}_{self.user.last_name}'.lower()
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.get_full_name()


class Model3D(models.Model):
    nome = models.CharField(max_length=255)
    sobre = models.TextField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Models 3D'

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome