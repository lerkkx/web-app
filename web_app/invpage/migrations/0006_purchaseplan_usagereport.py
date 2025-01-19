# Generated by Django 5.1.4 on 2025-01-13 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invpage", "0005_ownership"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchasePlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("planned_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("planned_supplier", models.CharField(max_length=255)),
                ("purchase_date", models.DateField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invpage.inventoryitem",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UsageReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notes", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invpage.inventoryitem",
                    ),
                ),
            ],
        ),
    ]
