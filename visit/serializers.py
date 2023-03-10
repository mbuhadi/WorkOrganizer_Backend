from rest_framework import serializers
from visit.models import Visit, ReturnTime
from school.models import School
from school.serializers import SchoolSerializer
from django.core.validators import RegexValidator
from employee.serializers import EmployeeSerializer


class DateTimeOfReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnTime
        fields = (
            "times",
        )


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"

