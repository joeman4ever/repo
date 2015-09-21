# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('dateCreated', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'created')),
                ('description', models.CharField(max_length=300, null=True)),
                ('category', models.CharField(default=b'Test', max_length=50)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('photos', models.ManyToManyField(to='picsite.Photo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
