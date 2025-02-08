from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *

class PurchasePlanForm(forms.ModelForm):
    class Meta:
        model = PurchasePlan
        fields = ['item', 'planned_price', 'planned_supplier', 'purchase_date']
        labels = {
            'item': _("Предмет"),
            'planned_price': _("Планируемая цена"),
            'planned_supplier': _("Планируемый поставщик"),
            'purchase_date': _("Дата покупки"),
        }

class UsageReportForm(forms.ModelForm):
    class Meta:
        model = UsageReport
        fields = ['user', 'item', 'notes']
        labels = {
            'user': _("Пользователь"),
            'item': _("Предмет"),
            'notes': _("Заметки"),
        }

class InventoryRequestForm(forms.ModelForm):
    class Meta:
        model = InventoryRequest
        fields = ['user', 'item', 'status', 'quantity']
        labels = {
            'user': _("Пользователь"),
            'item': _("Предмет"),
            'status': _("Статус"),
            'quantity': _("Количество"),
        }

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'status', 'quantity']
        labels = {
            'name': _("Название"),
            'description': _("Описание"),
            'status': _("Статус"),
            'quantity': _("Количество"),
        }
