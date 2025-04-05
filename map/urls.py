from django.urls import path
from .views import FiremanCoordinatesView, FiretruckCoordinatesView

urlpatterns = [
    path('fireman-coordinates/', FiremanCoordinatesView.as_view({"get": "list", "post": "create"}), name='fireman-coordinates'),
    path('fireman-coordinates/<int:pk>/', FiremanCoordinatesView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='fireman-coordinates-detail'),
    path('firetruck-coordinates/', FiretruckCoordinatesView.as_view({"get": "list", "post": "create"}), name='firetruck-coordinates'),
    path('firetruck-coordinates/<int:pk>/', FiretruckCoordinatesView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='firetruck-coordinates-detail'),
]
