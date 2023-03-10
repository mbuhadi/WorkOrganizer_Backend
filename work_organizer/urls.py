
from django.contrib import admin
from django.urls import path
from django.urls import path, include

COMMON_PATH = "api/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(COMMON_PATH + "employees/", include("employee.urls")),
    path(COMMON_PATH + "visits/", include("visit.urls")),
]
