from django.db import models
from django.contrib.auth.models import User


class Gestor(models.Model):
    sexo_choices = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    matricula= models.CharField(max_length=255)
    data_nascimento=models.DateField()
    sexo = models.CharField(max_length=255, choices=sexo_choices)
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return self.user.get_full_name()
    
    #please generete a unique username beased on the first and last name, and
    def save(self, *args, **kwargs):
        self.user.username = f'{self.user.first_name}_{self.user.last_name}'
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nome

class Model3D(models.Model):
    nome=models.CharField(max_length=255)
    # arquivo=models.FileField(upload_to='modelos_3d')
    sobre=models.TextField()
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Models 3D'

    def __str__(self) -> str:
        return self.nome
    
class Livro(models.Model):
    nome=models.CharField(max_length=255)
    autor=models.CharField(max_length=255)
    editora=models.CharField(max_length=255)
    localizacao=models.CharField(max_length=255)
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome