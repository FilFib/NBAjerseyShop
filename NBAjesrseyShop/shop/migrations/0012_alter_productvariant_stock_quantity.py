# Generated by Django 4.2.7 on 2023-12-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_orderproducts_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
