# Generated by Django 4.1.2 on 2022-10-19 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(max_length=10, unique=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('quantity', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('machine_deadline', models.DateField()),
                ('product', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='jobs.product')),
            ],
            options={
                'ordering': ['-create_date', '-start_date'],
            },
        ),
    ]