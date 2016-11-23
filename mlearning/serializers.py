from rest_framework import serializers
from .models import BodyType
from .models import Term
from .models import Topic
from .models import Lesson
from .models import LessonDetail
from .models import QuestionType
from .models import Question
from .models import Choice
from .models import Assessment
from .models import AssessmentChoice


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = '__all__'


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDetail
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lessondetails = LessonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class TermSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Term
        fields = '__all__'


class AssessmentChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentChoice
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    assessmentchoices = AssessmentChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = '__all__'
