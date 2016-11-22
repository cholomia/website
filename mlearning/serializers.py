from rest_framework import serializers
from .models import BodyType
from .models import Term
from .models import Topic
from .models import Lesson
from .models import LessonDetail


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    bodytype = BodyTypeSerializer(many=False, read_only=True)

    class Meta:
        model = LessonDetail
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lessondetails = LessonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class TermSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Term
        fields = '__all__'
