# Generated by Django 3.2.9 on 2022-01-10 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incident_reporter', '0006_alter_incidentreporter_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidentreporter',
            options={'verbose_name': 'Incident Reporter', 'verbose_name_plural': 'Incident Reporter'},
        ),
    ]
