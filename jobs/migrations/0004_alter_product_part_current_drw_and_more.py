# Generated by Django 4.1.2 on 2022-10-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_product_part_current_drw_product_part_current_rev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='part_current_drw',
            field=models.FileField(blank=True, max_length=10, upload_to='', verbose_name='Current PDF of Part Drawing'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op1',
            field=models.FileField(blank=True, max_length=10, upload_to='', verbose_name='1st GCode Attachment'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op2',
            field=models.FileField(blank=True, max_length=10, upload_to='', verbose_name='2nd GCode Attachment'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op3',
            field=models.FileField(blank=True, max_length=10, upload_to='', verbose_name='3rd GCode Attachment'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op4',
            field=models.FileField(blank=True, max_length=10, upload_to='', verbose_name='4th GCode Attachment'),
        ),
    ]
