from django.contrib import admin
from .models import InventoryItem, InventoryRequest

admin.site.register(InventoryItem)
admin.site.register(InventoryRequest)
