# Generated by Django 2.2.1 on 2019-05-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0010_auto_20190530_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_logo',
            field=models.ImageField(default='default.jpeg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='neighborhood_name',
            field=models.CharField(max_length=100),
        ),
    ]
