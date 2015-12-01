# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=1, choices=[('BO', 'Books'), ('MO', 'Movies'), ('AL', 'Musical Albums'), ('TV', 'TV Shows'), ('GA', 'Games')])),
                ('completion_date', models.DateField(help_text='The date of completion')),
                ('entry_created', models.DateTimeField(auto_now_add=True)),
                ('entry_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
