# Generated by Django 3.1.2 on 2021-02-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image_upload',
            field=models.ImageField(default='/Users/eomolo/projects/elijahomolosite/images/3f4eb74a-p-500x331.jpeg', upload_to=''),
            preserve_default=False,
        ),
    ]