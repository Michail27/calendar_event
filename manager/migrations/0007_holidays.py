# Generated by Django 3.1.5 on 2021-01-29 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20210127_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Праздник')),
                ('holiday_start', models.DateField(verbose_name='Начала праздника')),
                ('holiday_finish', models.DateField(verbose_name='Начала праздника')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.country')),
            ],
        ),
    ]
