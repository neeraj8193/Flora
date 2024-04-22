from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class FlowersOptionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(FlowersOption , FlowersOptionAdmin)

admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Subscription)
admin.site.register(SelectedFlowers)