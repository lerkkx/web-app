from django.conf import settings
from django.db import models

class InventoryRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='В ожидании')
    created_at = models.DateTimeField(auto_now_add=True)
    request_id = models.AutoField(primary_key=True)  
    quantity = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.item_name} - {self.status} (ID: {self.request_id}, Количество: {self.quantity})"


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Исправен')
    item_id = models.AutoField(primary_key=True)  
    quantity = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}, Количество: {self.quantity})"

class Ownership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_items')
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='owners')
    quantity = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f"{self.user.username} - {self.item.name} ({self.quantity})"


class PurchasePlan(models.Model):
    item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    planned_price = models.DecimalField(max_digits=10, decimal_places=2)
    planned_supplier = models.CharField(max_length=255)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.item.name} - {self.planned_supplier} (Date: {self.purchase_date})"

class UsageReport(models.Model):
    item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.item.name} (Created at: {self.created_at})"