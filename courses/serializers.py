from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Cours, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CoursSerializer(ModelSerializer):
    class Meta:
        model = Cours
        fields = "__all__"

class CourseDetailSerializer(ModelSerializer):
    count_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_count_of_lessons(self, obj):
        return obj.lessons.count()


    class Meta:
        model = Cours
        fields = ("name", "description", "count_of_lessons", "lessons")


