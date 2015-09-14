# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('loosecms_cas', '0003_auto_20150914_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cas_server_url', models.CharField(max_length=150, verbose_name='cas server url')),
                ('cas_logout_completely', models.BooleanField(default=False, verbose_name='cas logout completely')),
                ('cas_version', models.CharField(default=b'2', max_length=20, verbose_name='cas version', choices=[(b'1', b'Version 1'), (b'2', b'Version 2'), (b'3', b'Version 3'), (b'CAS_2_SAML_1_0', b'Version 2 with Saml')])),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Cas Configuration',
                'verbose_name_plural': 'Cas Configurations',
            },
        ),
        migrations.RemoveField(
            model_name='loosecmscasconfiguration',
            name='site',
        ),
        migrations.DeleteModel(
            name='LooseCMSCasConfiguration',
        ),
    ]
