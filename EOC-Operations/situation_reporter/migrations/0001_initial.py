# Generated by Django 3.2.9 on 2022-02-20 17:50

from django.db import migrations, models
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SituationReporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name of the Incident')),
                ('type', models.CharField(choices=[('Fire incident', 'Fire incident'), ('Road accident', 'Road accident'), ('Explosions', 'Explosions'), ('Armed conficts', 'Armed conficts'), ('Collapsed building', 'Collapsed building'), ('Waterbased accidents', 'Waterbased accidents'), ('Floods', 'Floods'), ('droughts', 'droughts'), ('Hail storms', 'Hail storms'), ('Land movement', 'Land movement'), ('Terror attacks', 'Terror attacks'), ('Other', 'other')], max_length=150, verbose_name='Type of the incident')),
                ('scene', models.CharField(max_length=150, verbose_name='Address where the incident')),
                ('geolocation', location_field.models.spatial.LocationField(srid=4326)),
                ('county', models.CharField(choices=[('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Mombasa', 'Mombasa'), ("Murang'a", "Murang'a"), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=18)),
                ('region', models.CharField(max_length=15)),
                ('source', models.CharField(max_length=150)),
                ('situation', models.TextField()),
                ('reported_time', models.TimeField()),
                ('arrival_time', models.DateTimeField()),
                ('dispatched_time', models.TimeField()),
                ('minor_cases', models.IntegerField()),
                ('critical_cases', models.IntegerField()),
                ('rescued', models.IntegerField()),
                ('missing', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('damage', models.CharField(max_length=255)),
                ('krcs_response', models.CharField(max_length=255)),
                ('cause', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Unconfirmed', 'Unconfirmed'), ('Archived', 'Archived')], max_length=13)),
                ('situation_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Situation Reporter',
                'verbose_name_plural': 'Situation Reporter',
            },
        ),
    ]
