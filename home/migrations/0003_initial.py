# Generated by Django 5.1.2 on 2024-11-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_remove_cartitem_cart_remove_cartitem_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
