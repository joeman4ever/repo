# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
                ('uploadDate', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'date')),
                ('uploadPath', models.ImageField(upload_to=b'images/%Y/%m/%d/', verbose_name=b'path')),
                ('caption', models.CharField(max_length=200, null=True)),
                ('longitude', models.IntegerField(null=True)),
                ('latitude', models.IntegerField(null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
