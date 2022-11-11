from django.contrib.gis.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from  django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.gis.geos import Point

from location_field.models.spatial import LocationField




class IncidentReporter(models.Model):


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

    GENDER_CHOICES =[
        ('Male','Male'),
        ('Female','Female'),
        ('Unknown','Unknown'),
    ]

    PURPOSE_CHOICES =[
        ('Psychosocial Support (PSS)','Psychosocial Support (PSS)'),
        ('Livelihood','Livelihood'),
        ('General Inquiry','General Inquiry'),
        ('Reporting Incident','Reporting Incident'),
        ('Membership & Volunteerism','Membership & Volunteerism'),
        ('Seeking Ambulance Services','Seeking Ambulance Services'),
        ('Covid-19','Covid-19'),
        ('Complaints & Feedback','Complaints & Feedback'),
        ('Food/ Financial Assistance','Food/ Financial Assistance'),
        ('Testing 1199 Hotline','Testing 1199 Hotline'),
        ('Infrastructural Damage','Infrastructural Damage'),
        ('TERA Messages','TERA Messages'),
        ('Reporting RTA','Reporting RTA'),
        ('SGBV','SGBV'),
        
    ]

    INTERVENTION_CHOICES =[

        ('On duty Counsellor','On duty Counsellor'),
        ('Advised accordingly','Advised accordingly'),
        ('Ref to Police','Ref to Police'),
        ('Ref to CC','Ref to CC'),
        ('Ref to Eplus','Ref to Eplus'),
        ('Ref to Other', 'Ref to Other'),
        ('Ref to Respective Agency', 'Ref to Respective Agency'),
        ('Ref to C&F Hotline','Ref to C&F Hotline'),
        ('Ref to Chief','Ref to Chief'),
        ('Not declared','Not declared'),
        ('PFA by Desk Officer','PFA by Desk Officer'),
        ('PFA','PFA'),
        ('Ref to 1196','Ref to 1196'),
        ('Ref to 719','Ref to 719'),
        ('Not declared','Not declared')
    ]

    STATUS_CHOICES =[
        ('Complete', 'Complete'),
        ('Pending', 'Pending'),
    ]

    
    desk_assistant = models.ForeignKey(settings.AUTH_USER_MODEL, editable= False ,on_delete=models.CASCADE, null =True)
    caller_name = models.CharField(_('Name of the caller'), null=True, max_length=75, blank= True)
    caller_gender = models.CharField(blank= True, null=True ,max_length=9, choices= GENDER_CHOICES)

    caller_age = models.PositiveIntegerField(blank= True, null=True, validators=[MinValueValidator(1), MaxValueValidator(140)],  \
        error_messages={'required':'Ensure that age is between 0 and 140 yrs'})
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', \
        message="Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed.")

    caller_phone_number = models.CharField(blank= True, null=True, validators=[phone_regex], max_length=14) # validators should be a list


    purpose = models.CharField(null=True,  choices= PURPOSE_CHOICES, max_length=75)
    intervention = models.CharField(null=True, choices= INTERVENTION_CHOICES, max_length=75)
    status = models.CharField(null=True, choices=STATUS_CHOICES, max_length=8)


    incident_date_time = models.DateTimeField(_("Date & Time"), auto_now=False, auto_now_add=False, \
        help_text="This field captures the date and time when the incident occured")

    
    
    address= models.CharField(blank= True, max_length=50, null=True,help_text="Type in the location / place where the \
        incident occurred in this field. Try to find out the exact location. This field automatically updates the map below")

    geolocation = LocationField(null=True, blank= True, based_fields=['address'], zoom=12)

    county= models.CharField(null=True, blank= True, max_length=15, choices= COUNTY_CHOICES)

    region = models.CharField(null=True, blank= True, max_length=13)

    comments = models.TextField (null=True, blank= True)
    
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)


    def save (self, *args, **kwargs):

        self.region = reverse_search_from_dictionary (krcs_regions, self.county)
        super(IncidentReporter, self).save( *args, **kwargs)



    class Meta:
        verbose_name = "Incident Reporter"
        verbose_name_plural = "Incident Reporter"
        indexes = [models.Index(fields=['caller_name'])]
        permissions = [
            ('export_data_csv','Can export data as a CSV'),
            ]






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
