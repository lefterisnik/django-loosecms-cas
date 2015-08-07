# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from loosecms.models import Plugin
from ckeditor.fields import RichTextField


class CasManager(Plugin):
    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give some title.'))
    description = RichTextField(_('description'))

    ctime = models.DateTimeField(editable=False, auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    image = models.ImageField(_('image'), upload_to='cas')

    published = models.BooleanField(_('published'), default=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


