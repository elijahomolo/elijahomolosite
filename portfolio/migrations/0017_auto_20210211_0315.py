# Generated by Django 3.1.2 on 2021-02-11 03:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20210211_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 3, 15, 47, 935939, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
