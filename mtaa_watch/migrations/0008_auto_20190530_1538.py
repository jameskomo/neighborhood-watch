# Generated by Django 2.2.1 on 2019-05-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0007_auto_20190530_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='neighborhood_name',
            field=models.CharField(choices=[('1', 'Red Ville'), ('2', 'Green View'), ('3', 'The Park'), ('4', 'Lil Arcade'), ('5', 'Komo Avenue')], max_length=50),
        ),
    ]
