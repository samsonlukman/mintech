# Generated by Django 4.1.7 on 2023-08-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0014_video_viewers_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarydocument',
            name='viewers_ip',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='librarydocument',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
