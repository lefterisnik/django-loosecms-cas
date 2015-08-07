# -*- coding: utf-8 -*-
from django.conf import settings

# CAS Settings
# TODO: Very simply implementation. Need to be changed
settings.AUTHENTICATION_BACKENDS += ('django_cas_ng.backends.CASBackend',)