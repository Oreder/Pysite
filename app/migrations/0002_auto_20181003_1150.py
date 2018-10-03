# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubuser',
            name='blog',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='location',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='public_gists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='public_repos',
            field=models.IntegerField(default=0),
        ),
    ]
