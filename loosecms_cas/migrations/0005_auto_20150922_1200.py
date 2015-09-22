# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_cas', '0004_auto_20150914_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cas',
            name='title',
            field=models.CharField(help_text='Give some title.', unique=True, max_length=200, verbose_name='title'),
        ),
    ]
