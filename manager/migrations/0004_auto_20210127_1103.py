# Generated by Django 3.1.5 on 2021-01-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20210127_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileuser',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='profileuser',
            unique_together={('email',)},
        ),
    ]
