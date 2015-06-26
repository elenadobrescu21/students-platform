# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_platform', '0002_auto_20150626_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
