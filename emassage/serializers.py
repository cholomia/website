import datetime

from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers

from .models import Course, Category, Lesson, Question, Choice, Forum, Comment, Grade, ForumVote, \
    CommentVote, VideoSimulation


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
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


class LessonSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    vote_count = serializers.SerializerMethodField()
    my_vote = serializers.SerializerMethodField()
    points = serializers.SerializerMethodField()

    def get_vote_count(self, obj):
        votes = CommentVote.objects.filter(comment=obj).aggregate(total_votes=Sum('vote')).get('total_votes')
        if votes is not None:
            return votes
        else:
            return 0

    def get_my_vote(self, obj):
        try:
            return CommentVote.objects.get(user=self.context['request'].user, comment=obj).vote
        except Exception as e:
            return 0

    def get_points(self, obj):
        epoch = datetime.datetime.utcfromtimestamp(0)
        naive = obj.created.replace(tzinfo=None)
        millis = (naive - epoch).total_seconds() * 1000.0
        vote_points = self.get_vote_count(obj) * 300000.0
        return millis + vote_points

    class Meta:
        model = Comment
        fields = ('id', 'forum', 'username', 'body', 'created', 'updated', 'vote_count', 'my_vote', 'points')


class ForumSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    comment_count = serializers.IntegerField(source='forum_comments.count', read_only=True)
    vote_count = serializers.SerializerMethodField()
    my_vote = serializers.SerializerMethodField()
    points = serializers.SerializerMethodField()

    def get_vote_count(self, obj):
        votes = ForumVote.objects.filter(forum=obj).aggregate(total_votes=Sum('vote')).get('total_votes')
        if votes is not None:
            return votes
        else:
            return 0

    def get_my_vote(self, obj):
        try:
            return ForumVote.objects.get(user=self.context['request'].user, forum=obj).vote
        except Exception as e:
            return 0

    def get_points(self, obj):
        epoch = datetime.datetime.utcfromtimestamp(0)
        naive = obj.created.replace(tzinfo=None)
        millis = (naive - epoch).total_seconds() * 1000.0
        vote_points = self.get_vote_count(obj) * 300000.0
        return millis + vote_points

    class Meta:
        model = Forum
        fields = ('id', 'username', 'title', 'content', 'created', 'updated', 'comment_count', 'vote_count', 'my_vote',
                  'points')


class GradeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Grade
        fields = ('id', 'lesson', 'raw_score', 'item_count', 'username')


class ForumVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumVote
        fields = ('vote', 'forum')


class CommentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVote
        fields = ('vote', 'comment')


class VideoSimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSimulation
        fields = '__all__'
