# Generated by Django 3.1.2 on 2021-02-09 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20210208_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 43, 50, 633118, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
