# Generated by Django 4.2.4 on 2023-09-27 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0022_sharepost_group_alter_sharepost_group_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharepost',
            name='group',
        ),
        migrations.RemoveField(
            model_name='sharepost',
            name='group_post',
        ),
    ]