# Generated by Django 3.2.21 on 2024-01-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cont', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('prev_price', models.IntegerField()),
                ('curr_price', models.IntegerField()),
                ('key_word', models.CharField(max_length=40)),
                ('content', models.ManyToManyField(related_name='content', to='UserView.Content')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]