
from django.db import migrations, connections
from django.contrib.auth.models import Group
from ..models import User


from ..constants import Groups


def create_groups(apps, schema_editor):
    Group.objects.create(name=Groups.Passenger.name)
    Group.objects.create(name=Groups.Driver.name)


def insert_to_groups(apps, schema_editor):
    g = Group.objects.get(name=Groups.Driver.name)
    users = User.objects.all()
    for u in users:
        g.user_set.add(u)


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0010_auto_20190731_1747'),
    ]

    operations = [
        migrations.RunPython(create_groups),
        migrations.RunPython(insert_to_groups),
    ]
