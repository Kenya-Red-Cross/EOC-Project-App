import csv

from django.contrib.gis import admin
from django.utils.translation import gettext as _
from django.http import HttpResponse
from leaflet.admin import LeafletGeoAdmin

from .models import SituationReporter   

class ExportCSVMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=incidents.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected Records"

class SituationReporterAdmin(admin.ModelAdmin, ExportCSVMixin):

   
    list_display = ('name','type','scene','county','situation_date')

    list_filter =('situation_date','type','county')
    search_fields = ['id']

    actions = ["export_as_csv"]

    
    fieldsets = (
        
        ('', {
            'fields': ('name', 'type','cause','situation','situation_date', 'status')}),
        ('', {
            'fields': ('scene', 'geolocation','county')}),

        ('', {
            'fields': ('reported_time','dispatched_time', 'arrival_time')}),

        ('', {
            'fields': ('rescued', 'minor_cases', 'critical_cases','missing','dead','damage')}),

        ('', {
            'fields': ('krcs_response',)}),


    )
        



admin.site.register(SituationReporter, SituationReporterAdmin)

#admin.site.site_header = "EOC Admin"
#admin.site.site_title = "HF Locator"
#admin.site.index_title = "Welcome to Incident Reporter"