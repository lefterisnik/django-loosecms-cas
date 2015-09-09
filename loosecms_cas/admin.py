# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Cas
from .plugin import CasPlugin

admin.site.register(Cas, CasPlugin)