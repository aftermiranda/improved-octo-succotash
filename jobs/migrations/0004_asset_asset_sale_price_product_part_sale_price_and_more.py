# Generated by Django 4.1.2 on 2022-11-01 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_product_part_current_drw_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_sale_price',
            field=models.CharField(blank=True, max_length=20, verbose_name='Sale Price, MSRP'),
        ),
        migrations.AddField(
            model_name='product',
            name='part_sale_price',
            field=models.CharField(blank=True, max_length=500, verbose_name='Part Sale Price'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_owner',
            field=models.CharField(blank=True, max_length=10, verbose_name='Asset Owner'),
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_product_name',
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_product_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Asset Product Name'),
        ),
    ]
