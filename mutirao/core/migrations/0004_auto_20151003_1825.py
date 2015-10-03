# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150926_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comofunciona',
            options={'verbose_name_plural': 'Como funciona', 'verbose_name': 'Como funciona'},
        ),
    ]
