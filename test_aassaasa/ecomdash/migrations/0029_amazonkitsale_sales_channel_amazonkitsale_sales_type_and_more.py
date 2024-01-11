# Generated by Django 4.2 on 2023-07-26 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ecomdash", "0028_saleschannel_treat_negative_sales_as_returns"),
    ]

    operations = [
        migrations.AddField(
            model_name="amazonkitsale",
            name="sales_channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="amazonkitsaleschannel",
                to="ecomdash.saleschannel",
            ),
        ),
        migrations.AddField(
            model_name="amazonkitsale",
            name="sales_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ecomdash.salestype",
            ),
        ),
        migrations.AddField(
            model_name="kitsale",
            name="sales_channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shopifykitsaleschannel",
                to="ecomdash.saleschannel",
            ),
        ),
        migrations.AddField(
            model_name="kitsale",
            name="sales_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ecomdash.salestype",
            ),
        ),
    ]
