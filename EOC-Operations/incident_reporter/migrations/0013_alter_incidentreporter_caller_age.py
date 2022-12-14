# Generated by Django 3.2.9 on 2022-01-23 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_reporter', '0012_alter_incidentreporter_caller_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_age',
            field=models.PositiveIntegerField(blank=True, error_messages={'required': 'Ensure that age is between 0 and 140 yrs'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(140)]),
        ),
    ]
