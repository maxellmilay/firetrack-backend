from django.contrib import admin
from incident.models import Incident, IncidentReport
# Register your models here.
admin.site.register(Incident)
admin.site.register(IncidentReport)
