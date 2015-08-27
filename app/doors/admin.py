from django.contrib import admin
from django.contrib.admin import ModelAdmin

from models import Door

class DoorAdmin(ModelAdmin):
    model = Door
    list_display = ('name', 'status')

admin.site.register(Door, DoorAdmin)
