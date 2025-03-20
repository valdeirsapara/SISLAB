from django.db import models

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