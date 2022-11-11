# Generated by Django 3.2.9 on 2022-06-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('situation_reporter', '0003_alter_situationreporter_krcs_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situationreporter',
            name='type',
            field=models.CharField(choices=[('Fire', 'Fire'), ('Road accident', 'Road accident'), ('Explosions', 'Explosions'), ('Armed conficts', 'Armed conficts'), ('Collapsed building', 'Collapsed building'), ('Waterbased accidents', 'Waterbased accidents'), ('Floods', 'Floods'), ('droughts', 'droughts'), ('Hail storms', 'Hail storms'), ('Land movement', 'Land movement'), ('Terror attacks', 'Terror attacks'), ('Other', 'other'), ('Criminal acts', 'Criminal acts'), ('Protest', 'Protest'), ('School Fires', 'School Fires')], max_length=150, verbose_name='Type of the incident'),
        ),
    ]