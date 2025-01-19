from django import forms
from .models import PurchasePlan, UsageReport

class PurchasePlanForm(forms.ModelForm):
    class Meta:
        model = PurchasePlan
        fields = ['item', 'planned_price', 'planned_supplier', 'purchase_date']

class UsageReportForm(forms.ModelForm):
    class Meta:
        model = UsageReport
        fields = ['item', 'notes']
