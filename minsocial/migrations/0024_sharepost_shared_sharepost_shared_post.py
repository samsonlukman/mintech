# Generated by Django 4.2.4 on 2023-09-27 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0023_remove_sharepost_group_remove_sharepost_group_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharepost',
            name='shared',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sharepost',
            name='shared_post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='minsocial.post'),
        ),
    ]
