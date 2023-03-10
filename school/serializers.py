from rest_framework import serializers
from school.models import School
from django.core.validators import RegexValidator


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            "name_ar",
        )