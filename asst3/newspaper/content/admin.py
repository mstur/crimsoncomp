# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Content, Article, Contributor

# Register your models here.
admin.site.register(Content)
admin.site.register(Article)
admin.site.register(Contributor)