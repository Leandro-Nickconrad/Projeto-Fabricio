# Generated by Django 3.2.6 on 2022-01-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título do Filme')),
                ('atalho', models.SlugField(unique=True, verbose_name='Atalho')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição do Filme')),
                ('nome_da_imagem', models.CharField(max_length=100, unique=True, verbose_name='Nome Img')),
                ('duracao', models.DurationField(verbose_name='Duração do Filme')),
                ('producao', models.CharField(max_length=255, verbose_name='Produção')),
                ('direcao', models.CharField(max_length=255, verbose_name='Direção')),
                ('esta_em_cartaz', models.BooleanField(default=False, verbose_name='Está em Cartaz')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Filme',
                'ordering': ['criado_em'],
            },
        ),
    ]
