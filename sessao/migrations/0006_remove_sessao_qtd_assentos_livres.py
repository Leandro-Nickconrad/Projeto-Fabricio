# Generated by Django 3.2.6 on 2022-02-05 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0005_sessao_num_sala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessao',
            name='qtd_assentos_livres',
        ),
    ]
