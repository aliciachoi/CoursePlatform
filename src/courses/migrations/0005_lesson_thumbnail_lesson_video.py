# Generated by Django 5.1.4 on 2024-12-11 18:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_lesson_can_preview_lesson_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
    ]
