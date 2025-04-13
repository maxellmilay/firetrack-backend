from django.urls import path, include
from user.views import UserView, SquadView, FirestationView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("manage/", UserView.as_view({"get": "list", "post": "create"}), name="user-list"),
    path("manage/<int:pk>/", UserView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="user-detail"),
    path("squads/", SquadView.as_view({"get": "list", "post": "create"}), name="squad-list"),
    path("squads/<int:pk>/", SquadView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="squad-detail"),
    path("firestations/", FirestationView.as_view({"get": "list", "post": "create"}), name="firestation-list"),
    path("firestations/<int:pk>/", FirestationView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="firestation-detail"),
]
