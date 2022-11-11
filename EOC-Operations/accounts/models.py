from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.gis.db import models
from django.contrib import admin
from  django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as gtlzy


# Create your models here.


class CustomAccountManager (BaseUserManager):
    
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.superuser = True
        user.staff = True
        user.save(using=self._db)
        return user

STATION_CHOICES = [
    ('HQ','HQ-South C'),
    ('Garissa','Garissa'),
    ('Garsen','Garsen'),
    ('Other', 'Other'),
]

REGION_CHOICES = [

    ('Central Region', 'Central Region'),
    ('Coast Region', 'Coast Region'),
    ('Lower Eastern Region', 'Lower Eastern Region'),
    ('North Eastern Region','North Eastern Region' ),
    ('North Rift Region', 'North Rift Region'),
    ('South Rift Region', 'South Rift Region'),
    ('Upper Eastern', 'Upper Eastern'),
    ('West Kenya Region','West Kenya Region'),
]


class UserProfile(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list

    email = models.EmailField( gtlzy('email address'), unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    #designation = models.CharField(max_length=50)
    #station = models.CharField(choices =STATION_CHOICES, max_length=25)
    region = models.CharField(choices =REGION_CHOICES,max_length=50)


    is_active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []
 
    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    @admin.display(description="Full Name")
    def get_full_name(self):
        return self.first_name  + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.superuser
