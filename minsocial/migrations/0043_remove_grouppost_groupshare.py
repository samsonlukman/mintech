# Generated by Django 4.2.4 on 2023-09-29 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0042_grouppost_groupshare_alter_groupshare_shared_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouppost',
            name='groupshare',
        ),
    ]