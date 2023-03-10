from django.contrib import admin
from .models import Employee, Degree, SubDepartment
# Register your models here.
admin.site.register(Employee)
admin.site.register(Degree)
admin.site.register(SubDepartment)