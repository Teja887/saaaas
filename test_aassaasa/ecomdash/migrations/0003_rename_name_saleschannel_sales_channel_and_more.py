# Generated by Django 4.2 on 2023-05-12 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0002_saleschannel_salestype_alter_subproduct_product_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="saleschannel",
            old_name="name",
            new_name="sales_channel",
        ),
        migrations.RenameField(
            model_name="salestype",
            old_name="name",
            new_name="sales_type",
        ),
    ]