# Generated by Django 3.1.2 on 2021-02-06 01:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_auto_20210206_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 1, 40, 33, 17479, tzinfo=utc), verbose_name='date updated'),
        ),
    ]