# Generated by Django 3.1.2 on 2021-02-09 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0018_auto_20210209_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 17, 38, 33, 526310, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
