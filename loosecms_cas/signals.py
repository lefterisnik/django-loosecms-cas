# -*- coding: utf-8 -*-
from django.conf import settings


def update_cas_settings(sender, instance, created, **kwargs):
    cas_configuration = instance

    if cas_configuration.cas_server_url:
        setattr(settings, 'CAS_SERVER_URL', cas_configuration.cas_server_url)

    setattr(settings, 'CAS_LOGOUT_COMPLETELY', cas_configuration.cas_logout_completely)
    setattr(settings, 'CAS_VERSION', cas_configuration.cas_version)
