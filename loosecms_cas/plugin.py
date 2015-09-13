# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin
from django_cas_ng.signals import cas_user_authenticated


def callback(sender, **kwargs):
    '''
    Store more data in database for logging
    :param sender:
    :param kwargs:
    :return: None
    '''
    return None


class CasPlugin(PluginModelAdmin):
    model = Cas
    name = _('CAS Login')
    template = "plugin/cas.html"
    plugin = True
    extra_initial_help = None
    cas_user_authenticated.connect(callback)

    def update_context(self, context, manager):
        context['casmanager'] = manager
        return context

plugin_pool.register_plugin(CasPlugin)