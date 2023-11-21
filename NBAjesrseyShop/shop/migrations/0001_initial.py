# Generated by Django 4.2.7 on 2023-11-20 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NbaPlayer",
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
                ("nba_player", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("payment_date", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(max_length=20)),
                ("total_cost", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("team", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=50)),
                ("image", models.ImageField(blank=True, null=True, upload_to="ście")),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("size", models.CharField(max_length=5)),
                ("stock_quantity", models.IntegerField(default=0)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "nba_player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.nbaplayer"
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.team"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderProducts",
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
                ("quantity", models.IntegerField()),
                (
                    "product_by_quan_coast",
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="shop.order"
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="shop.product"
                    ),
                ),
            ],
        ),
    ]
