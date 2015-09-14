# -*- coding: utf-8 -*-
from django.conf import settings
from django.apps import AppConfig, apps
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.db import ProgrammingError, OperationalError



class LooseCMSCasConfig(AppConfig):
    name = 'loosecms_cas'
    verbose_name = _('Loose CMS Plugin - Cas')

    def ready(self):
        # CAS Settings
        # TODO: Very simply implementation. Need to be changed
        settings.AUTHENTICATION_BACKENDS += ('django_cas_ng.backends.CASBackend',)

        # Get values for settings file
        SiteApp = apps.get_app_config('sites')
        Site = SiteApp.get_model('Site')
        try:
            current_site = Site.objects.get_current()
        except (ProgrammingError, OperationalError) as e:
            return
        except Site.DoesNotExist:
            raise ObjectDoesNotExist("In settings.py you set wrong SITE_ID. Please set the SITE_ID to match "
                                     "with these from database.")

        try:
            cas_configuration = current_site.casconfiguration
        except (ProgrammingError, OperationalError) as e:
            return
        except ObjectDoesNotExist:
            return

        cas_server_url = getattr(settings, 'CAS_SERVER_URL', None)
        if not cas_server_url and cas_configuration.cas_server_url:
            setattr(settings, 'CAS_SERVER_URL', cas_configuration.cas_server_url)

        cas_logout_completely = getattr(settings, 'CAS_LOGOUT_COMPLETELY', True)
        if cas_logout_completely != cas_configuration.cas_logout_completely:
            setattr(settings, 'CAS_LOGOUT_COMPLETELY', cas_configuration.cas_logout_completely)

        cas_version = getattr(settings, 'CAS_VERSION', '2')
        if cas_version != cas_configuration.cas_version:
            setattr(settings, 'CAS_VERSION', cas_configuration.cas_version)
