import csv
from django.contrib.auth import get_permission_codename

from django.contrib.gis import admin
from django.http import HttpResponse


#from leaflet.admin import LeafletGeoAdmin

#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields

from .models import IncidentReporter

class ExportCSVMixin:
    @admin.action(
        permissions =['delete'],
        description = "Export Selected Records",)

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names =      ['caller_gender','purpose','intervention','county','region','status','incident_date_time','desk_assistant']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=incidents.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


    #export_as_csv.short_description = "Export Selected Records"




class IncidentReporterAdmin(admin.ModelAdmin,ExportCSVMixin):

    #display_raw = True
    #map_width= "1200"
    #map_height = 700


    list_display = ('id','caller_name','purpose','county','incident_date_time','desk_assistant','status','created_at')

    list_filter =('incident_date_time','caller_gender','purpose','region','intervention','desk_assistant','created_at','status')
    search_fields = ['caller_name']

    actions = ["export_as_csv"]

    #formfield_overrides = {
    #    map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    #}

    fieldsets = (
        ('Incident Date', {
            'fields': ('incident_date_time',)}),
        ('Caller Details', {
            'fields': ('caller_name', 'caller_gender', 'caller_age',
                       'caller_phone_number')}),
        ('Caller/Incident Location', {
            'fields': ('county','address', 'geolocation')}),

        ('Other Details', {
            'fields': ('purpose', 'intervention','comments','status')}),
    )

    list_per_page = 100    
    #readonly_fields = ['desk_assistant']

    def save_model(self, request,obj, form, change ):
        if not obj.pk:
            obj.desk_assistant = request.user
        super().save_model(request,obj, form, change )

'''
    def has_export_data_csv_permission (self, request):

        """Does the user have export data permissions"""

        opts = self.opts
        codename = get_permission_codename ('export_data_csv',opts)
        return request.user.has_perm('%s.%s' %(opts.app_label, codename))
'''

admin.site.register(IncidentReporter,IncidentReporterAdmin)

#admin.site.site_header = "EOC Admin"
#admin.site.site_title = "HF Locator"
#admin.site.index_title = "Welcome to Incident Reporter"


