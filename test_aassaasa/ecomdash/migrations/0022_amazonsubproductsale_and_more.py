# Generated by Django 4.2 on 2023-07-20 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0021_rename_quantity_sold_kitsale_shopify_quantity_sold"),
    ]

    operations = [
        migrations.CreateModel(
            name="AmazonSubProductSale",
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
                ("amazon_date_of_sales", models.DateTimeField()),
                ("amazon_quantity_sold", models.IntegerField(default=0)),
                ("amazon_product_return", models.BooleanField(default=False)),
                ("amazon_orderid", models.CharField(default="DE101", max_length=1000)),
                (
                    "amazon_sales_channel",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sales",
                        to="ecomdash.saleschannel",
                    ),
                ),
                (
                    "amazon_sales_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ecomdash.salestype",
                    ),
                ),
                (
                    "amazon_sub_product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="amazonsubproductsales",
                        to="ecomdash.subproduct",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="shopifysubproductsale",
            name="shopify_sub_product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shopifysubproductsales",
                to="ecomdash.subproduct",
            ),
        ),
        migrations.DeleteModel(
            name="SubProductSale",
        ),
    ]