from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PatientSerializer
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('name')
    serializer_class = PatientSerializer