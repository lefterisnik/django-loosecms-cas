# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_cas', '0006_auto_20150922_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cas',
            name='slug',
            field=models.SlugField(help_text='Give the slug.', unique=True, verbose_name=b'slug'),
        ),
    ]
