# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cas',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give some title.', max_length=200, verbose_name='title')),
                ('description', loosecms.fields.LoosecmsRichTextField(verbose_name='description')),
                ('image', loosecms.fields.UploadFilePathField(recursive=True, upload_to=b'cas', blank=True, path=b'cas', verbose_name='image')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            bases=('loosecms.plugin',),
        ),
    ]
