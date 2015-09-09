# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from loosecms.models import Plugin
from loosecms.fields import LoosecmsRichTextField, UploadFilePathField


class Cas(Plugin):
    default_type = 'CasPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give some title.'))
    description = LoosecmsRichTextField(_('description'))

    image = UploadFilePathField(_('image'), upload_to='cas', path='cas', blank=True)

    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


