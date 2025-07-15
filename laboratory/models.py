from django.db import models


class Laboratory(models.Model):
    """Modelo para gerenciamento de laboratórios."""
    
    # Constants for status choices
    DISPONIVEL = 0
    INDISPONIVEL = 1

    ESTADO_CHOICES = (
        (DISPONIVEL, 'Disponível'),
        (INDISPONIVEL, 'Indisponível'),
    )

    nome = models.CharField(max_length=255, verbose_name='Nome')
    status = models.IntegerField(
        choices=ESTADO_CHOICES, 
        default=DISPONIVEL,
        verbose_name='Status'
    )
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_modificacao = models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')

    def __str__(self) -> str:
        return self.nome
    
    def is_disponivel(self) -> bool:
        """Verifica se o laboratório está disponível."""
        return self.status == self.DISPONIVEL and self.ativo
    
    class Meta:
        verbose_name = 'Laboratório'
        verbose_name_plural = 'Laboratórios'
        ordering = ['nome']
    