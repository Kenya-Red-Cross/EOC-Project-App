from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize   
from rest_framework import viewsets
from  django_filters import rest_framework as  filters

from .models import IncidentReporter
from .incident_filters import IncidentFilters 
from .incident_serializer import IncidentReporterSerializer

 #ViewSets define the view behavior.

class IncidentReporterViewSet(viewsets.ModelViewSet):

    queryset = IncidentReporter.objects.all()
    serializer_class =  IncidentReporterSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = IncidentFilters



class HomePageView (TemplateView):

    template_name = 'incident_reporter/index.html'

@login_required
def incident_dataset(request):

    incidents = serialize  ('geojson',IncidentReporter.objects.all() )
    return HttpResponse (incidents, content_type='json')