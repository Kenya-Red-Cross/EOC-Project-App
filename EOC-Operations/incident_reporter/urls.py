from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import IncidentReporterViewSet, HomePageView, incident_dataset


router = routers.DefaultRouter()
router.register(r'incidentreporter', IncidentReporterViewSet)

urlpatterns = [

    path('', HomePageView.as_view(), name ='index'),
    path('incident_data',incident_dataset,name='incident_data'),
    path ('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),

]
