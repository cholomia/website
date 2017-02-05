from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, CourseList, CreateUserView, LoginView, ForumViewSet, CommentViewSet, GradeViewSet, \
    ValidationView, ForumVoteViewSet, CommentVoteViewSet, VideoSimulationViewSet, TwistWordViewSet, CategoryList, \
    AnnouncementViewSet, GalleryViewSet

app_name = 'emassage'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses-paginated', CourseViewSet)
router.register(r'forums', ForumViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'forum-vote', ForumVoteViewSet)
router.register(r'comment-vote', CommentVoteViewSet)
router.register(r'video-simulations', VideoSimulationViewSet)
router.register(r'twist-words', TwistWordViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'galleries', GalleryViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^courses/', view=CourseList.as_view()),
    url(r'^user/register/', view=CreateUserView.as_view()),
    url(r'^user/login/', view=LoginView.as_view()),
    url(r'^user/validation/', view=ValidationView.as_view()),
    url(r'^categories/', view=CategoryList.as_view()),
]
