from django.contrib import admin
from .models import InventoryItem, InventoryRequest, PurchasePlan, UsageReport

admin.site.register(InventoryItem)
admin.site.register(InventoryRequest)
admin.site.register(PurchasePlan)
admin.site.register(UsageReport)
