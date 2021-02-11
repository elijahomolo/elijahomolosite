# Generated by Django 3.1.2 on 2021-01-23 02:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date published')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(default='no content yet', max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 1, 23, 2, 27, 47, 389883, tzinfo=utc), verbose_name='date updated')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publish?')),
                ('author', models.ForeignKey(default='Elijah Omolo', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='uncategorized', on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]