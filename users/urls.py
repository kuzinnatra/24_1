from django.urls import path
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from users.views import (UserCreateApiView, UserDestroyApiView,
                         UserListApiView, UserRetrieveApiView, UserUpdateApiView, PaymentCreateApiView, PaymentDestroyApiView,
                         PaymentListApiView, PaymentRetrieveApiView, PaymentUpdateApiView)

app_name = UsersConfig.name


urlpatterns = [
    path('payment/create/', PaymentCreateApiView.as_view(), name='payment-create'),
    path('payment/', PaymentListApiView.as_view(), name='payment-list'),
    path('payment/<int:pk>/', PaymentRetrieveApiView.as_view(), name='payment-retrieve'),
    path('payment/<int:pk>/update/', PaymentUpdateApiView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', PaymentDestroyApiView.as_view(), name='payment-delete'),
    path('users/create/', UserCreateApiView.as_view(), name='user-create'),
    path('users/', UserListApiView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveApiView.as_view(), name='user-retrieve'),
    path('users/<int:pk>/update/', UserUpdateApiView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDestroyApiView.as_view(), name='user-delete'),
]