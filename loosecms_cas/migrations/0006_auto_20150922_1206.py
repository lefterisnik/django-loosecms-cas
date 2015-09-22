# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify
from django.db import models, migrations
import loosecms.fields

try:
    from unidecode import unidecode
except ImportError:
    unidecode = lambda slug: slug


def generate_slug_cas(apps, schema_editor):
    Cas = apps.get_model('loosecms_cas', 'Cas')
    for cas in Cas.objects.all():
        cas.slug = slugify(unidecode(cas.title))
        cas.save()


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_cas', '0005_auto_20150922_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='cas',
            name='header_title',
            field=models.CharField(default='Cas login', help_text='Give the title of the panel.', max_length=150, verbose_name='header title'),
        ),
        migrations.AddField(
            model_name='cas',
            name='slug',
            field=models.SlugField(help_text='Give the slug.', verbose_name=b'slug'),
        ),
        migrations.AlterField(
            model_name='cas',
            name='description',
            field=loosecms.fields.LoosecmsRichTextField(help_text='Give the description of the panel.', verbose_name='description'),
        ),
        migrations.RunPython(generate_slug_cas),
    ]