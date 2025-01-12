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


