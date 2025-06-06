# Generated by Django 5.1.7 on 2025-03-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrib', '0002_noticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobre', models.TextField()),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
