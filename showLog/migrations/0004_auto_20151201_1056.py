# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showLog', '0003_auto_20151201_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='type',
        ),
        migrations.AddField(
            model_name='entry',
            name='ent_type',
            field=models.CharField(verbose_name='type', choices=[('BO', 'Book'), ('MO', 'Movie'), ('AL', 'Musical Album'), ('TV', 'TV Show'), ('GA', 'Game')], max_length=30, default='BO'),
        ),
    ]
