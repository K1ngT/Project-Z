from django.contrib import admin

# Register your models here.
from .models import Asset, Locations

admin.site.register(Asset)
admin.site.register(Locations)