from  django_filters import rest_framework as  filters
from .models import IncidentReporter


class IncidentFilters (filters.FilterSet):

    purpose = filters.CharFilter ( field_name ="purpose",lookup_expr ="iexact")
    region  = filters.CharFilter (lookup_expr ="iexact")
    county = filters.CharFilter (lookup_expr ="iexact")

    class Meta:
        model = IncidentReporter
        fields =['purpose','region','county']



