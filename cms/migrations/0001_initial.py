# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-03 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
            ],
        ),
    ]
