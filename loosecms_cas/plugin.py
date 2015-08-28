# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

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
    model = CasManager
    name = _('CAS Login')
    form = CasManagerForm
    template = "plugin/cas.html"
    plugin = True
    extra_initial_help = None
    cas_user_authenticated.connect(callback)
    fields = ('type', 'placeholder', 'title', 'description', 'image', 'published')

    def update_context(self, context, manager):
        context['casmanager'] = manager
        return context

    def get_changeform_initial_data(self, request):
        initial = {}
        if self.extra_initial_help:
            initial['type'] = self.extra_initial_help['type']
            initial['placeholder'] = self.extra_initial_help['placeholder']
            initial['manager'] = self.extra_initial_help['page']

            return initial
        else:
            return {'type': 'CasPlugin'}

plugin_pool.register_plugin(CasPlugin)