from django.apps import AppConfig


class IncidentReporterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'incident_reporter'

    def ready(self):

        from .scheduler  import scheduler
        scheduler.start()