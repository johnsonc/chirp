# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='accounts.UserProfile'),
        ),
    ]
