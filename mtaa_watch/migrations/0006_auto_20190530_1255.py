# Generated by Django 2.2.1 on 2019-05-30 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0005_auto_20190530_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaa_watch.Neighborhood'),
        ),
    ]
