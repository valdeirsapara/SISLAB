from django.db import models

# Create your models here.
class Laboratory(models.Model):
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
    