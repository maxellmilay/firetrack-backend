from django.urls import path
from .views import CoordinatesView, LatestUserCoordinatesView

urlpatterns = [
    path('coordinates/', CoordinatesView.as_view({"get": "list", "post": "create"}), name='coordinates'),
    path('coordinates/<int:pk>/', CoordinatesView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='coordinates-detail'),
    path('coordinates/latest/<str:tracker_id>/', LatestUserCoordinatesView.as_view(), name='latest-user-coordinates'),
]
