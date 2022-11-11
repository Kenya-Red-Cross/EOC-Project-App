# Generated by Django 3.2.9 on 2022-05-27 12:01

import django.core.validators
from django.db import migrations, models
import location_field.models.spatial


class Migration(migrations.Migration):

    dependencies = [
        ('incident_reporter', '0013_alter_incidentreporter_caller_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreporter',
            name='address',
            field=models.CharField(blank=True, help_text='Type in the location / place where the         incident occurred in this field. Try to find out the exact location.             This field automatically updates the map below', max_length=255),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Intersex', 'Intersex')], max_length=9),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_name',
            field=models.CharField(blank=True, max_length=75, verbose_name='Name of the caller'),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='caller_phone_number',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,14}$')]),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='county',
            field=models.CharField(blank=True, choices=[('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Mombasa', 'Mombasa'), ("Murang'a", "Murang'a"), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=18),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='geolocation',
            field=location_field.models.spatial.LocationField(blank=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='incidentreporter',
            name='region',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
