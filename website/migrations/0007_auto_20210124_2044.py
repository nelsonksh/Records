# Generated by Django 3.1.5 on 2021-01-24 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210121_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='due',
            name='query',
            field=models.DateField(default=datetime.date(2021, 1, 24)),
        ),
    ]
