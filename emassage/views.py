import django_filters.filters
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Comment, Forum, Grade, UserProfile, ForumVote, CommentVote, VideoSimulation, TwistWord, \
    Category, Announcement, Gallery
from .permissions import IsOwnerOrReadOnly
from .serializers import CourseSerializer, UserSerializer, CommentSerializer, ForumSerializer, GradeSerializer, \
    ForumVoteSerializer, CommentVoteSerializer, VideoSimulationSerializer, TwistWordSerializer, CategorySerializer, \
    AnnouncementSerializer, GallerySerializer
from rest_framework.filters import OrderingFilter


# Create your views here.

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CourseList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        serializer = UserSerializer(user, many=False)
        if user is not None:
            try:
                user_profile = UserProfile.objects.get(user=user, enable=True)
                if user_profile is not None:
                    return JsonResponse({'success': True, 'message': "Login Successful", 'user': serializer.data})
                else:
                    return JsonResponse({'success': False, 'message': "Email Address not yet validated"})
            except Exception as e:
                return JsonResponse({'success': False, 'message': "Email Address not yet validated"})
        else:
            return JsonResponse({'success': False, 'message': "Login Failed"})


class ValidationView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(username=request.GET['username'])
            if user is not None:
                user_profile = UserProfile.objects.get(user=user, validation_code=request.GET['validation_code'])
                if user_profile is not None:
                    user_profile.enable = True
                    user_profile.save()
                    return JsonResponse({'success': True, 'message': "Email Validation Successful"})
                else:
                    return JsonResponse({'success': False, 'message': "Invalid Code"})
            else:
                return JsonResponse({'success': False, 'message': "Username does not exist"})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': "Invalid Validation"})


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ('created', 'updated', 'points')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentFilter(django_filters.rest_framework.FilterSet):
    forum_id = django_filters.NumberFilter(name="forum__id")
    username = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Comment
        fields = ['forum_id', 'username']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = CommentFilter
    ordering_fields = ('id', 'created', 'updated',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GradeFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Grade
        fields = ['username']


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = GradeFilter
    pagination_class = None

    def get_object(self):
        if self.request.method == 'PUT':
            obj, created = Grade.objects.get_or_create(pk=self.kwargs.get('pk'),
                                                       defaults={'lesson_id': self.request.data['lesson'],
                                                                 'user': self.request.user,
                                                                 'raw_score': self.request.data['raw_score'],
                                                                 'item_count': self.request.data['item_count'],
                                                                 'try_count': self.request.data['try_count']})
            return obj
        else:
            return super(GradeViewSet, self).get_object()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ForumVoteViewSet(viewsets.ModelViewSet):
    queryset = ForumVote.objects.all()
    serializer_class = ForumVoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        if self.request.method == 'PUT':
            obj, created = ForumVote.objects.get_or_create(pk=self.kwargs.get('pk'),
                                                           defaults={'forum_id': self.request.data['forum'],
                                                                     'user': self.request.user,
                                                                     'vote': self.request.data['vote']})
            return obj
        else:
            return super(ForumVoteViewSet, self).get_object()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentVoteViewSet(viewsets.ModelViewSet):
    queryset = CommentVote.objects.all()
    serializer_class = CommentVoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        if self.request.method == 'PUT':
            obj, created = CommentVote.objects.get_or_create(pk=self.kwargs.get('pk'),
                                                             defaults={'comment_id': self.request.data['comment'],
                                                                       'user': self.request.user,
                                                                       'vote': self.request.data['vote']})
            return obj
        else:
            return super(CommentVoteViewSet, self).get_object()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoSimulationViewSet(viewsets.ModelViewSet):
    queryset = VideoSimulation.objects.all()
    serializer_class = VideoSimulationSerializer
    pagination_class = None


class TwistWordViewSet(viewsets.ModelViewSet):
    queryset = TwistWord.objects.all()
    serializer_class = TwistWordSerializer
    pagination_class = None


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    pagination_class = None


class GalleryFilter(django_filters.rest_framework.FilterSet):
    category_id = django_filters.NumberFilter(name="category__id")

    class Meta:
        model = Gallery
        fields = ['category_id', ]


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filter_class = GalleryFilter
