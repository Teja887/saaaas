# Generated by Django 4.2 on 2023-07-20 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0020_kitsale_shopify_default_order_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kitsale",
            old_name="quantity_sold",
            new_name="shopify_quantity_sold",
        ),
    ]
