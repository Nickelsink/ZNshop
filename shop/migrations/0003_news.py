# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-30 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_goods_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazva', models.CharField(max_length=50)),
                ('telo', models.TextField()),
            ],
        ),
    ]
