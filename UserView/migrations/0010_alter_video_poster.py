# Generated by Django 3.2.21 on 2024-01-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0009_auto_20240123_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='poster',
            field=models.ImageField(blank=True, default='media/Screen Shot 2024-01-15 at 05.01.44.png', upload_to='posters/'),
        ),
    ]
