# Generated by Django 4.1.7 on 2023-08-13 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minsocial', '0009_remove_announcement_announcement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementpostimage',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_post_images', to='minsocial.announcement'),
        ),
    ]
