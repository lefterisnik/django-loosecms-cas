# -*- coding: utf-8 -*-
from django.conf.urls import url

app_urlpatterns = [
    url(r'^accounts/login/$', 'django_cas_ng.views.login', name='cas_login'),
    url(r'^accounts/logout/$', 'django_cas_ng.views.logout', name='cas_logout'),
]

urlpatterns = []


