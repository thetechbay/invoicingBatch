# Generated by Django 4.2.7 on 2023-12-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_address_clients_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='invoice_date',
            field=models.DateField(),
        ),
    ]