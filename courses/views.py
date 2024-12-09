from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from courses.models import Cours
from courses.serializers import CoursSerializer


class CoursViewSet(ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
