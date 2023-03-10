from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from employee.models import Employee, Degree
from employee.serializers import EmployeeSerializer, DegreeSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

class EmployeesList(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SpecificEmployee(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer