# Generated by Django 5.1.7 on 2025-03-20 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrib', '0005_livro_localizacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Laboratorio',
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
