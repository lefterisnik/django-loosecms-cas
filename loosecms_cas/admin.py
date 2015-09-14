# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Cas, CasConfiguration
from .plugin import CasPlugin


class CasConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site', 'cas_server_url', 'cas_logout_completely', 'cas_version')


admin.site.register(Cas, CasPlugin)
admin.site.register(CasConfiguration, CasConfigurationAdmin)