# Generated by Django 3.1.2 on 2021-02-10 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20210209_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 16, 30, 35, 907220, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
