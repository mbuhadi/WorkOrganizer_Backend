from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from visit import views

urlpatterns = [
    path("", views.VisitsList.as_view(), name="employees"),
    path("<pk>", views.SpecificVisit.as_view(), name="visit"),
]

# {"get": "retrieve", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}