# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CasManager
from .plugin import CasPlugin

admin.site.register(CasManager, CasPlugin)