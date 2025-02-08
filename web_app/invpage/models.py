from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.utils import timezone

class InventoryItem(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    status = models.CharField(max_length=50, default='Исправен', verbose_name=_("Статус"))
    item_id = models.AutoField(primary_key=True)  
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Количество"))

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}, Количество: {self.quantity})"

    class Meta:
        verbose_name = _("предмет инвентаря")
        verbose_name_plural = _("Предметы инвентаря")


class InventoryRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, verbose_name=_("Предмет"))
    status = models.CharField(max_length=50, default='В ожидании', verbose_name=_("Статус"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    request_id = models.AutoField(primary_key=True)  
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Количество"))



    def __str__(self):
        return f"{self.item.name} - {self.status} (ID: {self.request_id}, Количество: {self.quantity})"

    class Meta:
        verbose_name = _("запрос на инвентарь")
        verbose_name_plural = _("Запросы на инвентарь")




class Ownership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_items', verbose_name=_("Пользователь"))
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='owners', verbose_name=_("Инвентарь"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Количество"))

    def __str__(self):
        return f"{self.user.username} - {self.item.name} ({self.quantity})"



class PurchasePlan(models.Model):
    item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, verbose_name=_("Инвентарь"))
    planned_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Планируемая цена"))
    planned_supplier = models.CharField(max_length=255, verbose_name=_("Планируемый поставщик"))
    purchase_date = models.DateField(verbose_name=_("Дата покупки"))

    def __str__(self):
        return f"{self.item.name} - {self.planned_supplier} (Date: {self.purchase_date})"

    class Meta:
        verbose_name = _("план закупки")
        verbose_name_plural = _("Планы закупок")


class UsageReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь"), default=1)
    item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, verbose_name=_("Инвентарь"))
    notes = models.TextField(verbose_name=_("Заметки"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        local_time = timezone.localtime(self.created_at)
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"Отчет для {self.item.name} (Пользователь: {self.user.username}, Создано: {formatted_time})"

    class Meta:
        verbose_name = _("отчет об использовании")
        verbose_name_plural = _("Отчеты об использовании")
