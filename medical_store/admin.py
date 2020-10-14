import json 
from django.contrib import admin
# from .models import *

admin.site.register(CompanyDetails)
admin.site.register(Purchase)
admin.site.register(PurchaseInventory)
admin.site.register(MedicineInventory)
admin.site.register(Sales)
admin.site.register(SalesInventory)


# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
#admin.site.register(StoreDetails)

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#           'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
#     }

# admin.site.register(MedicineInventory)
# admin.site.register(Purchase)
# admin.site.register(PurchaseInventory)
