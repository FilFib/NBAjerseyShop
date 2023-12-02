# Generated by Django 4.2.7 on 2023-11-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_nba_player_alter_product_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nba_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.nbaplayer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.team'),
        ),
    ]