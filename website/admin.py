# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from mysite.website.models import UserProfiles

admin.site.register(UserProfiles)

