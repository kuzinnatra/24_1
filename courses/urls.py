from rest_framework.routers import SimpleRouter

from courses.views import CoursViewSet
from courses.apps import CoursesConfig

app_name = CoursesConfig.name



router = SimpleRouter()
router.register('', CoursViewSet)

urlpatterns = []

urlpatterns += router.urls