# -*- coding: utf-8 -*-
from django.conf import settings
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LooseCMSCasConfig(AppConfig):
    name = 'loosecms_cas'
    verbose_name = _('Loose CMS Plugin - Cas')

    def ready(self):
        # CAS Settings
        # TODO: Very simply implementation. Need to be changed
        settings.AUTHENTICATION_BACKENDS += ('django_cas_ng.backends.CASBackend',)