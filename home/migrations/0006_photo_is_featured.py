# Generated by Django 5.1.2 on 2024-10-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
