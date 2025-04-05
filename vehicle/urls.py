from django.urls import path
from .views import FiretruckView

urlpatterns = [
    path('firetrucks/', FiretruckView.as_view({"get": "list", "post": "create"}), name='firetruck-list'),
    path('firetrucks/<int:pk>/', FiretruckView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='firetruck-detail'),
]
