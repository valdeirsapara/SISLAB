from django.db import models

# Create your models here.
class News(models.Model):
    titulo=models.CharField(max_length=255)
    conteudo=models.TextField()
    ativo=models.BooleanField(default=True)
    data_criacao=models.DateTimeField(auto_now_add=True)
    data_modificacao=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo