# Generated by Django 4.1.2 on 2022-11-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='part_current_drw',
            field=models.FileField(blank=True, max_length=50, upload_to='', verbose_name='Current PDF of Part Drawing'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_current_rev',
            field=models.CharField(blank=True, max_length=25, verbose_name='Current Revision'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_image_file',
            field=models.FileField(blank=True, max_length=50, upload_to='', verbose_name='Image of the Part'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op1',
            field=models.FileField(blank=True, max_length=50, upload_to='', verbose_name='1st GCode Attachment'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op2',
            field=models.FileField(blank=True, max_length=50, upload_to='', verbose_name='2nd GCode Attachment'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_manf_op3',
            field=models.FileField(blank=True, max_length=50, upload_to='', verbose_name='3rd GCode Attachment'),
        ),
    ]
