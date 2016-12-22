from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, CourseList, CreateUserView, LoginView, ForumViewSet, CommentViewSet

app_name = 'emassage'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses-paginated', CourseViewSet)
router.register(r'forums', ForumViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^courses/', view=CourseList.as_view()),
    url(r'^user/register/', view=CreateUserView.as_view()),
    url(r'^user/login/', view=LoginView.as_view()),
]
