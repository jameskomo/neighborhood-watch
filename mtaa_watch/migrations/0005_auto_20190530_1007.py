# Generated by Django 2.2.1 on 2019-05-30 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa_watch', '0004_contact_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
