# Generated by Django 3.1.2 on 2021-02-05 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20210205_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 18, 36, 49, 949944, tzinfo=utc), verbose_name='date updated'),
        ),
    ]