# Generated by Django 4.1.7 on 2023-08-13 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0003_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
    ]