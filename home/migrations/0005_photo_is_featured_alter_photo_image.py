# Generated by Django 5.1.2 on 2024-10-24 11:58

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_photo_description_alter_photo_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
