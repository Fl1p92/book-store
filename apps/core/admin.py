from django.contrib import admin

from . import models


admin.site.register(models.LogLine)
admin.site.register(models.Request)
