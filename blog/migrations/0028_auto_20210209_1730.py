# Generated by Django 3.1.2 on 2021-02-09 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20210209_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 17, 30, 9, 106892, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
