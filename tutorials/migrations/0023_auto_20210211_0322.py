# Generated by Django 3.1.2 on 2021-02-11 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0022_auto_20210211_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='body',
            field=markdownx.models.MarkdownxField(default='no content yet', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 3, 22, 54, 698916, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
