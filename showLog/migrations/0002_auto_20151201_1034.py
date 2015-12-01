# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showLog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='type',
            field=models.CharField(choices=[('BO', 'Book'), ('MO', 'Movie'), ('AL', 'Musical Album'), ('TV', 'TV Show'), ('GA', 'Game')], max_length=30),
        ),
    ]
