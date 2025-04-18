from django.urls import path
from .views import IncidentView, IncidentReportView

urlpatterns = [
    path('', IncidentView.as_view({"get": "list", "post": "create"}), name='incident-list'),
    path('<int:pk>/', IncidentView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='incident-detail'),
    path('reports/', IncidentReportView.as_view({"get": "list", "post": "create"}), name='incident-report-list'),
    path('reports/<int:pk>/', IncidentReportView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='incident-report-detail'),
]
