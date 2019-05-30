# Generated by Django 2.2.1 on 2019-05-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0002_auto_20190530_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_number', models.TextField()),
                ('contact_address', models.TextField()),
                ('contact_logo', models.ImageField(default='default.jpeg', upload_to='images/')),
            ],
        ),
    ]
