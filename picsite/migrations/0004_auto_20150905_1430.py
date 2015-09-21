# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picsite', '0003_auto_20150905_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='category',
            field=models.CharField(default=b'Test', max_length=50, verbose_name=b'category'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=300, null=True, verbose_name=b'description'),
        ),
    ]
