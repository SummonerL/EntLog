# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showLog', '0002_auto_20151201_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='completion_date',
            field=models.DateField(help_text='The date of completion.'),
        ),
    ]
