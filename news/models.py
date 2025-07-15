from django.db import models


class News(models.Model):
    """Modelo para notícias do sistema."""
    
    titulo = models.CharField(max_length=255, verbose_name='Título')
    conteudo = models.TextField(verbose_name='Conteúdo')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_modificacao = models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['-data_criacao']