from rest_framework import serializers
from employee.models import Employee, Degree, SubDepartment
from django.core.validators import RegexValidator

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = (
            "name_ar",
        )

class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = (
            "name_ar",
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "name_ar",
            "national_id",
            "file_number",
            "degree",
            "occupation_name"
        )