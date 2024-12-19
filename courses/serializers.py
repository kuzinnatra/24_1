from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from courses.models import Cours, Lesson, Subscription
from courses.validators import YoutubeValidators


class LessonSerializer(ModelSerializer):
    validators = [YoutubeValidators(field='video_url')]
    class Meta:
        model = Lesson
        fields = "__all__"


class CoursSerializer(ModelSerializer):
    lessons = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def get_lessons(self, cours):
        return [lesson.name for lesson in Lesson.objects.filter(cours=cours)]

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False
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
        fields = ("name", "description", "count_of_lessons", "lessons", "owner")



class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'