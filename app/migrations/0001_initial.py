# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('blog', models.CharField(max_length=128)),
                ('public_gists', models.IntegerField()),
                ('public_repos', models.IntegerField()),
                ('avatar_url', models.URLField()),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('location', models.TextField(max_length=256)),
            ],
        ),
    ]
