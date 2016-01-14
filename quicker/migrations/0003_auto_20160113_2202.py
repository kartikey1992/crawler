# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicker', '0002_car_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='site_id',
        ),
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(default=b'Delhi', max_length=300),
        ),
    ]
