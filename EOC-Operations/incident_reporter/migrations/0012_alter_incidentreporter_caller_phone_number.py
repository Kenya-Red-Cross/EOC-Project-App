# Generated by Django 3.2.9 on 2022-01-23 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_reporter', '0011_alter_incidentreporter_desk_assistant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_phone_number',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,14}$')]),
        ),
    ]
