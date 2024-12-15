from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cours, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user22@sky.pro')
        self.cours = Cours.objects.create(name='Основы языка Python', description='Азы программирования на Python')
        self.lesson = Lesson.objects.create(name='Что такое программа?', cours=self.cours, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        '''тест на создание курса'''
        self.client.force_authenticate(user=self.user)
        url = reverse('courses:lessons_create')
        data = {
            'name': 'Урок 1',
            'description': 'Алгоритмы',
            'cours': self.cours.pk,
            'owner': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_create_lesson_Youtube(self):
        '''тест на урок со ссылкой на ютуб'''
        url = reverse('courses:lessons_create')
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Урок 1',
            'description': 'Алгоритмы',
            'cours': self.cours.pk,
            'owner': self.user.pk,
            'video_url': 'https://www.youtube.com/875656/'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_create_lesson_no_Youtube(self):
        '''тест на урок со ссылкой отличной от ютуб'''
        url = reverse('courses:lessons_create')
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Урок 1',
            'description': 'Алгоритмы',
            'cours': self.cours.pk,
            'owner': self.user.pk,
            'video_url': 'https://www.myvideo.com/34542/'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.count(), 1)

    def test_lesson_retrieve(self):
        '''тест на просмотр урока'''
        url = reverse('courses:lessons_retrieve', args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        '''тест на обновление урока'''
        url = reverse('courses:lessons_update', args=(self.lesson.pk,))
        data = {
            'name': 'Урок 2',
            'description': 'Повторение',
            'cours': self.cours.pk,
            'owner': self.user.pk
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), 'Урок 2')

    def test_lesson_delete(self):
        '''тест на удаление урока'''
        self.client.force_authenticate(user=self.user)
        url = reverse('courses:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_list(self):
        url = reverse('courses:lessons_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class CoursTestCase(APITestCase):

    # def setUp(self):
    #     self.user = User.objects.create(email='user22@sky.pro')
    #     self.cours = Cours.objects.create(name='Основы языка Python', description='Азы программирования на Python')
    #     self.client.force_authenticate(user=self.user)

    # def test_create_cours(self):
    #     '''тест на создание курса'''
    #     self.client.force_authenticate(user=self.user)
    #     url = reverse('courses:coursses-list')
    #     data = {
    #         'name': 'Мой первый курс',
    #         'description': 'Самый первый курс'
    #     }
    #     response = self.client.post(url, data)
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_update_cours(self):
    #     '''тест на обновление курса'''
    #     self.client.force_authenticate(user=self.user)
    #     url = reverse('courses:coursses-detail', args=(self.cours.pk,))
    #     data = {'name': 'Новая версия курса'}
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user344@sky.pro')
        self.course = Cours.objects.create(name='Курс 7', description='Описание курса 7')
        self.lesson = Lesson.objects.create(name='первый урок курса 7', cours=self.course, owner=self.user)
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        Subscription.objects.all().delete()
        url = reverse('courses:subscription_create')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Вы подписались')
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
        url = reverse('courses:subscription_create')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Вы отписались')

    def test_subscription_list(self):
        url = reverse('courses:subscription_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['course'], self.course.id)

    def test_subscribe_to_course_no_ex(self):
        Subscription.objects.all().delete()
        url = reverse('courses:subscription_create')
        data = {'course_id': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_subscribe_to_course_no_au(self):
        Subscription.objects.all().delete()
        self.client.force_authenticate(user='')
        url = reverse('courses:subscription_create')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)