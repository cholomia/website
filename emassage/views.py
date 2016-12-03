from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.http import JsonResponse

from .models import Course
from .serializers import CourseSerializer, UserSerializer


# Create your views here.

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


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
        if user is not None:
            return JsonResponse({'success': True, 'message': "Login Successful"})
        else:
            return JsonResponse({'success': False, 'message': "Login Failed"})
