from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import User, UserDetails
# from django.contrib.gis.db.models import GeometryField
# from django.forms.widgets import TextInput
# from mapwidgets.widgets import GooglePointFieldInlineWidget



# class PointLocation(admin.ModelAdmin):
#     formfield_overrides = {
#         GeometryField: {'widget': GooglePointFieldInlineWidget}
#     }

admin.site.register(User)
admin.site.register(UserDetails, LeafletGeoAdmin)
