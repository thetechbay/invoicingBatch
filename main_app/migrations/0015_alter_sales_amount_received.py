# Generated by Django 4.2.7 on 2023-12-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_payment_transaction_id_payment_sale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='amount_received',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]