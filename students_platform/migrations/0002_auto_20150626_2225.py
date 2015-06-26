# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, verbose_name='Upload a file', upload_to='media', null=True),
        ),
    ]
