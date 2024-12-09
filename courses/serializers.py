from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer

from courses.models import Cours, Lesson


class CoursSerializer(ModelSerializer):
    class Meta:
        model = Cours
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
