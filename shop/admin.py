from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(VendorProfile)
admin.site.register(FlowersOption)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Subscription)
admin.site.register(Address)
admin.site.register(Vendor)

@admin.register(SelectedFlowers)
class SelectedFlowersAdmin(admin.ModelAdmin):
    '''Admin View for SelectedFlowers'''

    list_display = ('user','flower','subscription','quantity','created_at')
