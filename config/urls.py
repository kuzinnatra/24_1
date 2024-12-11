from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls", namespace="courses")),
    path("users/", include("users.urls", namespace="users")),
]
