# Generated by Django 2.2.1 on 2019-05-30 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0003_remove_neighborhood_neighborhood_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaa_watch.Neighborhood'),
        ),
    ]
