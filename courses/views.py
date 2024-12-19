from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from courses.models import Cours, Lesson, Subscription
from courses.paginators import CustomPagination
from courses.serializers import CoursSerializer, LessonSerializer, CourseDetailSerializer, SubscriptionSerializer
from users.permissions import IsModer, IsOwner
from rest_framework.permissions import IsAuthenticated
from users.tasks import sub_update


class CoursViewSet(ModelViewSet):
    queryset = Cours.objects.all()
    pagination_class = CustomPagination
    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CoursSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    def update(self, request, pk=None):
        course = get_object_or_404(Cours, pk=pk)
        serializer = self.get_serializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            sub_update.delay(pk)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (~IsModer, IsAuthenticated,)


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner, )


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    (IsAuthenticated, IsModer | IsOwner,)


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer,)


class SubscriptionAPIView(APIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Cours, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'Вы отписались'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Вы подписались'
        return Response({"message": message})


class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()