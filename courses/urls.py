from django.urls import path
from rest_framework.routers import SimpleRouter
from courses.apps import CoursesConfig
from courses.views import (CoursViewSet, LessonCreateApiView,
                           LessonDestroyApiView, LessonListApiView,
                           LessonRetrieveApiView, LessonUpdateApiView, SubscriptionAPIView, SubscriptionListAPIView)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register(r'coursses', CoursViewSet, basename='coursses')

urlpatterns = [
    path('lessons/', LessonListApiView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>', LessonRetrieveApiView.as_view(), name='lessons_retrieve'),
    path('lessons/create/', LessonCreateApiView.as_view(), name='lessons_create'),
    path('lessons/<int:pk>/delete/',LessonDestroyApiView.as_view(),name='lessons_delete'),
    path('lessons/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lessons_update'),
    path('subscription/create/', SubscriptionAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
]

urlpatterns += router.urls
