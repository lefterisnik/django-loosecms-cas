# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from loosecms.models import Plugin
from loosecms.fields import LoosecmsRichTextField, UploadFilePathField

from .signals import update_cas_settings


class Cas(Plugin):
    default_type = 'CasPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give some title.'))
    description = LoosecmsRichTextField(_('description'))

    image = UploadFilePathField(_('image'), upload_to='cas', path='cas', blank=True)

    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class CasConfiguration(models.Model):
    VERSION_1 = '1'
    VERSION_2 = '2'
    VERSION_3 = '3'
    VERSION_2_SAML = 'CAS_2_SAML_1_0'
    choices = (
        (VERSION_1, 'Version 1'),
        (VERSION_2, 'Version 2'),
        (VERSION_3, 'Version 3'),
        (VERSION_2_SAML, 'Version 2 with Saml'),
    )

    site = models.OneToOneField(Site)

    cas_server_url = models.CharField(_('cas server url'), max_length=150)

    cas_logout_completely = models.BooleanField(_('cas logout completely'), default=False)

    cas_version = models.CharField(_('cas version'), choices=choices, default=VERSION_2, max_length=20)

    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Cas Configuration')
        verbose_name_plural = _('Cas Configurations')


post_save.connect(update_cas_settings, CasConfiguration)
