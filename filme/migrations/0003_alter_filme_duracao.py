# Generated by Django 3.2.6 on 2022-06-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_alter_filme_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='duracao',
            field=models.TextField(verbose_name='Duração do Filme'),
        ),
    ]
