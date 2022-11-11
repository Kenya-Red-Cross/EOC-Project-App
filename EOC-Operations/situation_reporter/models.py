from re import S
from django.contrib.gis.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from  django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

from location_field.models.spatial import LocationField

# Create your models here.


class SituationReporter (models.Model):

    TYPE_CHOICES = [
        ('Fire','Fire'),
        ('Road accident', 'Road accident'),
        ('Explosions', 'Explosions'),
        ('Armed conficts', 'Armed conficts'),
        ('Collapsed building', 'Collapsed building'),
        ('Sea/Lake Incidents','Sea/Lake Incidents'),
        ('Floods','Floods'),
        ('Drought','Drought'),
        ('Hail storms','Hail storms'),
        ('Land movement','Land movement'),
        ('Terror attacks','Terror attacks'),
        ('Criminal acts','Criminal acts'),
        ('Protest','Protest'),
        ('School Fires','School Fires'),
        ('Other','other'),
    ]
    STATUS_CHOICES = [
        ('Active','Active'),
        ('Unconfirmed','Unconfirmed'),
        ('Archived', 'Archived'),
    ]

    COUNTY_CHOICES = [
        
        ("Baringo", "Baringo"),
        ("Bomet", "Bomet"),
        ("Bungoma","Bungoma"),
        ("Busia", "Busia"),
        ("Elgeyo Marakwet", "Elgeyo Marakwet"),
        ("Embu",	"Embu"),
        ("Garissa", "Garissa"),
        ("Homa Bay", "Homa Bay"),
        ("Isiolo", "Isiolo"),
        ("Kajiado", "Kajiado"),
        ("Kakamega", "Kakamega"),
        ("Kericho", "Kericho"),
        ("Kiambu", "Kiambu"),
        ("Kilifi", "Kilifi"),
        ("Kirinyaga", "Kirinyaga"),
        ("Kisii", "Kisii"),
        ("Kisumu", "Kisumu"),
        ("Kitui", "Kitui"),
        ("Kwale", "Kwale"),
        ("Laikipia", "Laikipia"),
        ("Lamu", "Lamu"),
        ("Machakos", "Machakos"),
        ("Makueni", "Makueni"),
        ("Mandera", "Mandera"),
        ("Marsabit", "Marsabit"),
        ("Meru", "Meru"),
        ("Migori", "Migori"),
        ("Mombasa", "Mombasa"),
        ("Murang'a", "Murang'a"),
        ("Nairobi", "Nairobi"),
        ("Nakuru", "Nakuru"),
        ("Nandi", "Nandi"),
        ("Narok", "Narok"),
        ("Nyamira", "Nyamira"),
        ("Nyandarua", "Nyandarua"),
        ("Nyeri", "Nyeri"),
        ("Samburu", "Samburu"),
        ("Siaya", "Siaya"),
        ("Taita Taveta", "Taita Taveta"),
        ("Tana River", "Tana River"),
        ("Tharaka Nithi", "Tharaka Nithi"),
        ("Trans Nzoia", "Trans Nzoia"),
        ("Turkana", "Turkana"),
        ("Uasin Gishu", "Uasin Gishu"),
        ("Vihiga", "Vihiga"),
        ("Wajir", "Wajir"),
        ("West Pokot", "West Pokot"),
    ]

    name = models.CharField (_("Name of the Incident"), max_length=150)
    type = models.CharField (_("Type of the incident"),choices= TYPE_CHOICES, max_length=150)
    scene = models.CharField(_("Address where the incident occured"), max_length=150)
    geolocation = LocationField(based_fields=['scene'], zoom=12)
    county= models.CharField(max_length=18, choices= COUNTY_CHOICES)
    
    region = models.CharField(max_length=15)

    source = models.CharField(max_length=150)
    situation = models.TextField() 

    reported_time = models.TimeField()
    arrival_time = models.DateTimeField()
    dispatched_time = models.TimeField()


    minor_cases = models.IntegerField()
    critical_cases = models.IntegerField()
    rescued = models.IntegerField()
    missing = models.IntegerField()
    dead = models.IntegerField()
    damage = models.CharField(max_length=255)

    krcs_response = models.TextField()
    cause = models.CharField(max_length=255)

    status = models.CharField(max_length=13, choices= STATUS_CHOICES)

    situation_date = models.DateTimeField()

   
    

    def save (self, *args, **kwargs):

        self.region = reverse_search_from_dictionary (krcs_regions, self.county)
        super(SituationReporter, self).save( *args, **kwargs)

    class Meta:
        verbose_name = "Situation Reporter"
        verbose_name_plural = "Situation Reporter"



def reverse_search_from_dictionary(dictionary, keyword):
    for key, values in dictionary.items():
        if keyword in values:
            return key

krcs_regions = {

    'Coast' :['Mombasa','Kilifi','Kwale','Lamu','Tana River','Taita Taveta'],
    'Central' : [ 'Kiambu','Kirinyaga',"Murang'a",'Nyeri','Meru','Tharaka Nithi','Embu','Laikipia'],
    'Lower Eastern' : ['Kajiado','Makueni','Kitui','Nairobi','Machakos' ],
    'North Eastern' : [ 'Garissa','Mandera','Wajir'],
    'North Rift' : [ 'Turkana','West Pokot','Trans Nzoia','Bungoma','Uasin Gishu','Nandi','Elgeyo Marakwet'],
    'South Rift' : [ 'Baringo','Nakuru','Nyandarua','Kericho','Bomet','Narok'],
    'Upper Eastern' : ['Isiolo','Samburu','Marsabit' ],
    'West Kenya' : [ 'Homa Bay','Migori','Kisii','Nyamira','Kisumu','Vihiga','Kakamega','Busia','Siaya'],

}

    


