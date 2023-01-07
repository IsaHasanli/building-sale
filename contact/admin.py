from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Contact, Message

admin.site.register(Contact, LeafletGeoAdmin)
admin.site.register(Message)