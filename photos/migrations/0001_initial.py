# Generated by Django 5.1.2 on 2024-11-03 12:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('size', models.CharField(default='8x10 inches', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]