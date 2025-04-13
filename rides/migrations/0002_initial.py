# Generated by Django 5.2 on 2025-04-11 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rides", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="ride",
            name="id_driver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="driver",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="ride",
            name="id_rider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rider",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="rideevent",
            name="id_ride",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rides.ride"
            ),
        ),
    ]
