# -*- coding:utf-8 -*-
from .models import CasManager
from loosecms.forms import PluginForm


class CasManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = CasManager