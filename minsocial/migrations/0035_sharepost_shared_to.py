# Generated by Django 4.2.4 on 2023-09-28 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0034_rename_timestamps_sharepost_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharepost',
            name='shared_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
