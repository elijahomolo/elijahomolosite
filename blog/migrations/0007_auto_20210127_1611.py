# Generated by Django 3.1.2 on 2021-01-27 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210127_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 16, 11, 37, 223041, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
