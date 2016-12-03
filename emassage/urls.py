from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, CourseList, CreateUserView, LoginView

app_name = 'emassage'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses-paginated', CourseViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^api/courses/', view=CourseList.as_view()),
    url(r'^api/user/register/', view=CreateUserView.as_view()),
    url(r'^api/user/login/', view=LoginView.as_view()),
]
