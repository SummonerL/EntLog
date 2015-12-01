# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showLog', '0004_auto_20151201_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last modified'),
        ),
    ]
