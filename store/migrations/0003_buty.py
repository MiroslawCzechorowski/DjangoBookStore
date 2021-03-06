# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20170107_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('size', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]
