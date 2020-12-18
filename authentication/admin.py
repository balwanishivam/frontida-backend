from django.contrib import admin
from .models import User, UserDetails
from leaflet.admin import LeafletGeoAdmin

admin.site.register(User)
admin.site.register(UserDetails, LeafletGeoAdmin)
