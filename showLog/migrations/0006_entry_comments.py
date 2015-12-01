# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showLog', '0005_auto_20151201_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='comments',
            field=models.TextField(verbose_name='additional comments', null=True, blank=True, max_length=320),
        ),
    ]
