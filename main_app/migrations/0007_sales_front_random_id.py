# Generated by Django 4.2.7 on 2023-12-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_sales_amount_received_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='front_random_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
