# Generated by Django 3.1.2 on 2021-02-06 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='body',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='author',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='featured',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 1, 20, 55, 184920, tzinfo=utc), verbose_name='date updated'),
        ),
    ]