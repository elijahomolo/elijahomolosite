# Generated by Django 3.1.2 on 2021-02-06 01:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210205_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 1, 2, 35, 635576, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
