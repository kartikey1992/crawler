# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='company',
            field=models.ForeignKey(default=1, to='quicker.Car_Company'),
            preserve_default=False,
        ),
    ]
