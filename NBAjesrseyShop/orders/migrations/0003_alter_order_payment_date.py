# Generated by Django 4.2.7 on 2023-12-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_address_id_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
