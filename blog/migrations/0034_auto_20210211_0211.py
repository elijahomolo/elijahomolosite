# Generated by Django 3.1.2 on 2021-02-11 02:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20210211_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 2, 11, 5, 914312, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
