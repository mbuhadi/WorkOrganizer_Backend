from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employee import views

urlpatterns = [
    path("", views.EmployeesList.as_view({"get": "list", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="employees"),
    path("<pk>", views.SpecificEmployee.as_view(), name="employee"),
]

# {"get": "retrieve", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}