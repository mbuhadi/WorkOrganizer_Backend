from django.shortcuts import render
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from visit.models import Visit
from visit.serializers import VisitSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponseRedirect

class VisitsList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class SpecificVisit(generics.RetrieveAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
