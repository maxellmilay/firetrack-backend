from django.urls import path, include
from .views import TeamView, FiremanView, IncidentCommanderView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("teams/", TeamView.as_view({"get": "list", "post": "create"}), name="team-list"),
    path("teams/<int:pk>/", TeamView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="team-detail"),
    path("firemen/", FiremanView.as_view({"get": "list", "post": "create"}), name="fireman-list"),
    path("firemen/<int:pk>/", FiremanView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="fireman-detail"),
    path("incident-commanders/", IncidentCommanderView.as_view({"get": "list", "post": "create"}), name="incident-commander-list"),
    path("incident-commanders/<int:pk>/", IncidentCommanderView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="incident-commander-detail"),
]
