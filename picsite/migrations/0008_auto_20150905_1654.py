# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picsite', '0007_auto_20150905_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Album Description'),
        ),
    ]
