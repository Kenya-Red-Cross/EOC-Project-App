from rest_framework.decorators import authentication_classes
from  django_filters import rest_framework as  filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import IncidentReporter



class IncidentReporterSerializer (GeoFeatureModelSerializer):

    
    class Meta:
        
        model = IncidentReporter
        geo_field = 'geolocation'

        
        exclude = ('caller_age','comments','created_at','desk_assistant')

        extra_kwargs = {'caller_name':{'write_only':True},'caller_phone_number':{'write_only':True},
         'comments':{'write_only':True},  'address':{'write_only':True}}