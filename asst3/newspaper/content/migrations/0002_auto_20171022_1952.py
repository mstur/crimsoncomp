# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='contribuotrs',
            new_name='contributors',
        ),
    ]
