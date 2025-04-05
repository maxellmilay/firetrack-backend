from django.urls import path
from .views import IncidentView, TravelOrderView, IncidentReportView

urlpatterns = [
    path('incidents/', IncidentView.as_view({"get": "list", "post": "create"}), name='incident-list'),
    path('incidents/<int:pk>/', IncidentView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='incident-detail'),
    path('travel-orders/', TravelOrderView.as_view({"get": "list", "post": "create"}), name='travel-order-list'),
    path('travel-orders/<int:pk>/', TravelOrderView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='travel-order-detail'),
    path('incident-reports/', IncidentReportView.as_view({"get": "list", "post": "create"}), name='incident-report-list'),
    path('incident-reports/<int:pk>/', IncidentReportView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='incident-report-detail'),
]
