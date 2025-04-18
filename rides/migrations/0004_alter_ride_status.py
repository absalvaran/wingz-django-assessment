# Generated by Django 5.2 on 2025-04-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rides", "0003_alter_ride_status_alter_rideevent_id_ride"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ride",
            name="status",
            field=models.CharField(
                choices=[
                    ("enroute", "en-route"),
                    ("pickup", "pickup"),
                    ("dropoff", "dropoff"),
                ],
                default="ENROUTE",
                max_length=50,
            ),
        ),
    ]
