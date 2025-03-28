# Generated by Django 5.1.4 on 2025-02-08 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="InventoryItem",
            fields=[
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "status",
                    models.CharField(
                        default="Исправен", max_length=50, verbose_name="Статус"
                    ),
                ),
                ("item_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="Количество"),
                ),
            ],
            options={
                "verbose_name": "предмет инвентаря",
                "verbose_name_plural": "Предметы инвентаря",
            },
        ),
        migrations.CreateModel(
            name="InventoryRequest",
            fields=[
                (
                    "status",
                    models.CharField(
                        default="В ожидании", max_length=50, verbose_name="Статус"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                ("request_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="Количество"),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invpage.inventoryitem",
                        verbose_name="Предмет",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "запрос на инвентарь",
                "verbose_name_plural": "Запросы на инвентарь",
            },
        ),
        migrations.CreateModel(
            name="Ownership",
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
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="Количество"),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owners",
                        to="invpage.inventoryitem",
                        verbose_name="Инвентарь",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owned_items",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
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
                (
                    "planned_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Планируемая цена"
                    ),
                ),
                (
                    "planned_supplier",
                    models.CharField(
                        max_length=255, verbose_name="Планируемый поставщик"
                    ),
                ),
                ("purchase_date", models.DateField(verbose_name="Дата покупки")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invpage.inventoryitem",
                        verbose_name="Инвентарь",
                    ),
                ),
            ],
            options={
                "verbose_name": "план закупки",
                "verbose_name_plural": "Планы закупок",
            },
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
                ("notes", models.TextField(verbose_name="Заметки")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invpage.inventoryitem",
                        verbose_name="Инвентарь",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "отчет об использовании",
                "verbose_name_plural": "Отчеты об использовании",
            },
        ),
    ]
