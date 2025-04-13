from django.urls import path
from .views import CoordinatesView

urlpatterns = [
    path('coordinates/', CoordinatesView.as_view({"get": "list", "post": "create"}), name='coordinates'),
    path('coordinates/<int:pk>/', CoordinatesView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='coordinates-detail'),
]
