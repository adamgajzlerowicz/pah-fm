# Generated by Django 2.1.2 on 2019-08-06 15:55

from django.db import migrations, connections

from ..constants import Groups


def insert_groups(apps, schema_editor):
    with connections['default'].cursor() as cursor:
        cursor.execute(f"INSERT INTO auth_group (\"name\") values ('{Groups.Passenger.name}')")
        cursor.execute(f"INSERT INTO auth_group (\"name\") values ('{Groups.Driver.name}')")


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0010_auto_20190731_1747'),
    ]

    operations = [
        migrations.RunPython(insert_groups),
    ]
