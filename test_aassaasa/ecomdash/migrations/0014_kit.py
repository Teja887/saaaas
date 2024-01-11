# Generated by Django 4.2 on 2023-07-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0013_alter_subproduct_sp_sku"),
    ]

    operations = [
        migrations.CreateModel(
            name="Kit",
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
                ("name", models.CharField(max_length=1000)),
                ("image", models.CharField(max_length=1000)),
                ("sp_sku", models.CharField(max_length=20, unique=True)),
                (
                    "sub_products",
                    models.ManyToManyField(
                        related_name="kits", to="ecomdash.subproduct"
                    ),
                ),
            ],
        ),
    ]
