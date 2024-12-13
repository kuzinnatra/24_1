from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from courses.models import Cours, Lesson
from courses.serializers import CoursSerializer, LessonSerializer, CourseDetailSerializer
from users.permissions import IsModer


class CoursViewSet(ModelViewSet):
    queryset = Cours.objects.all()
    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CoursSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer,)
        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (~IsModer,)


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (~IsModer,)
