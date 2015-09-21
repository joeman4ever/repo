# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picsite', '0004_auto_20150905_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='category',
            field=models.CharField(default=b'Test', max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
