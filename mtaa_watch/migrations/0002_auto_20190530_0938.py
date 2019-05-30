# Generated by Django 2.2.1 on 2019-05-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_image',
            field=models.ImageField(default='default.jpeg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='neighborhood_image',
            field=models.ImageField(default='default.jpeg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpeg', upload_to='images/'),
        ),
    ]
