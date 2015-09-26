# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sobre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComoFunciona',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, verbose_name='Título da Página')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sobre',
            options={'verbose_name_plural': 'Sobre', 'verbose_name': 'Sobre'},
        ),
    ]
