# Generated by Django 3.1.2 on 2021-02-08 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210208_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 18, 1, 4, 751157, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
