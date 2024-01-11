# Generated by Django 4.2 on 2023-07-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0023_amazonkitsale"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="amazonkitsale",
            name="amazon_order_id",
        ),
        migrations.AddField(
            model_name="amazonkitsale",
            name="amazon_orderid",
            field=models.CharField(default="DE101", max_length=50),
        ),
        migrations.AlterField(
            model_name="amazonsubproductsale",
            name="amazon_orderid",
            field=models.CharField(default="DE101", max_length=50),
        ),
    ]
