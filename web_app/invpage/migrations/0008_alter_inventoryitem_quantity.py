# Generated by Django 5.1.5 on 2025-01-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invpage", "0007_alter_inventoryitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventoryitem",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
