from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    DISPONIVEL =0
    INDISPONIVEL = 1

    ESTADO_CHOICE = (
        (DISPONIVEL, 'Disponível'),
        (INDISPONIVEL, 'Indisponível'),
    )

    nome=models.CharField(max_length=255)
    status = models.IntegerField(choices=ESTADO_CHOICE, default=DISPONIVEL)
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome
    

class Noticia(models.Model):
    titulo=models.CharField(max_length=255)
    conteudo=models.TextField()
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo
    

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