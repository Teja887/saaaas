# Generated by Django 4.2 on 2023-06-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0009_remove_productsale_order_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="productsale",
            name="orderid",
            field=models.CharField(default="DE101", max_length=1000),
        ),
    ]