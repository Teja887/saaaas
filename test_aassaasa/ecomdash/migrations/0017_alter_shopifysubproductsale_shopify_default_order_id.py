# Generated by Django 4.2 on 2023-07-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0016_rename_orderid_subproductsale_amazon_orderid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopifysubproductsale",
            name="shopify_default_order_id",
            field=models.BigIntegerField(),
        ),
    ]
