# Generated by Django 3.1.2 on 2021-02-05 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210128_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 17, 11, 11, 272706, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
