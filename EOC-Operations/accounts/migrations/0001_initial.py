# Generated by Django 3.2.9 on 2021-12-29 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('region', models.CharField(choices=[('Central Region', 'Central Region'), ('Coast Region', 'Coast Region'), ('Lower Eastern Region', 'Lower Eastern Region'), ('North Eastern Region', 'North Eastern Region'), ('North Rift Region', 'North Rift Region'), ('South Rift Region', 'South Rift Region'), ('Upper Eastern', 'Upper Eastern'), ('West Kenya Region', 'West Kenya Region')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('superuser', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]