# Generated by Django 3.2.9 on 2021-12-29 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_reporter', '0002_auto_20211229_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_age',
            field=models.PositiveIntegerField(blank=True, error_messages={'required': 'Ensure that age is between 0 and 140 yrs'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(140)]),
        ),
    ]