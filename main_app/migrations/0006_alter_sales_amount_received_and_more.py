# Generated by Django 4.2.7 on 2023-12-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_salesitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='amount_received',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='discount_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='discount_percent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='subtotal',
            field=models.FloatField(max_length=10000000),
        ),
        migrations.AlterField(
            model_name='sales',
            name='tax_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='tax_percent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salesitem',
            name='price',
            field=models.FloatField(),
        ),
    ]
