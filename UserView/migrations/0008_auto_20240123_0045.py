# Generated by Django 3.2.21 on 2024-01-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0007_video_drive_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='content',
        ),
        migrations.RemoveField(
            model_name='package',
            name='curr_price',
        ),
        migrations.RemoveField(
            model_name='package',
            name='key_word',
        ),
        migrations.RemoveField(
            model_name='package',
            name='prev_price',
        ),
        migrations.AddField(
            model_name='package',
            name='field',
            field=models.CharField(choices=[('videography', 'Videography'), ('cinema', 'Cinema')], default='videography', max_length=20),
        ),
        migrations.AddField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, upload_to='packages/'),
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
