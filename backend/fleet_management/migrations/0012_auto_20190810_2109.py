# Generated by Django 2.1.2 on 2019-08-10 21:09

from django.db import migrations, models

from ..models import Drive


def default_is_verified(apps, schema_editor):
    drives = Drive.objects.all()
    for drive in drives:
        drive.isVerified=True


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0011_add_default_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(default_is_verified),

    ]
