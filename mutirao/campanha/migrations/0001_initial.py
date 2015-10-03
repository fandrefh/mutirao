# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Campanha')),
                ('descricao', models.TextField(verbose_name='Finalidade')),
                ('local', models.CharField(max_length=250, verbose_name='Local')),
                ('data_campanha', models.DateField(verbose_name='Data')),
                ('horario', models.TimeField(verbose_name='Horário')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
