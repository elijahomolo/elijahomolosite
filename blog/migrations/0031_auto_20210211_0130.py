# Generated by Django 3.1.2 on 2021-02-11 01:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20210210_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 1, 30, 40, 279298, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
