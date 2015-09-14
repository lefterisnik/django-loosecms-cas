# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_cas', '0002_loosecmscasconfiguration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loosecmscasconfiguration',
            name='cas_url',
        ),
        migrations.AddField(
            model_name='loosecmscasconfiguration',
            name='cas_server_url',
            field=models.CharField(default='https://sso.sch.gr/', max_length=150, verbose_name='cas server url'),
            preserve_default=False,
        ),
    ]
