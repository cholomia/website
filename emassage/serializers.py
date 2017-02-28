import datetime
import uuid
from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers
from django.core.mail import send_mail

from .models import Course, Category, Lesson, Question, Choice, Forum, Comment, Grade, ForumVote, \
    CommentVote, VideoSimulation, UserProfile, TwistWord, Announcement, Gallery, LessonDetail


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        my_uuid = uuid.uuid4()
        validation_code = str(my_uuid)
        user_profile = UserProfile.objects.create(
            user=user,
            validation_code=validation_code,
            enable=False
        )
        user_profile.save()
        send_mail("EMassage Registration Validation",
                  "Please validate your account using the link: "
                  + "http://vlitztrom.pythonanywhere.com/emassage/api/user/validation/?username=" + user.username
                  + "&validation_code=" + validation_code,
                  "capstone2tip.@gmail.com", [user.email])
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


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDetail
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    detail_lessons = LessonDetailSerializer(many=True, read_only=True)

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
        fields = ('id', 'lesson', 'raw_score', 'item_count', 'username', 'try_count')


class ForumVoteSerializer(serializers.ModelSerializer):
    forum_votes = ForumSerializer(source='forum', read_only=True)

    class Meta:
        model = ForumVote
        fields = ('vote', 'forum', 'forum_votes')


class CommentVoteSerializer(serializers.ModelSerializer):
    comment_votes = CommentSerializer(source='comment', read_only=True)

    class Meta:
        model = CommentVote
        fields = ('vote', 'comment', 'comment_votes')


class VideoSimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSimulation
        fields = '__all__'


class TwistWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwistWord
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
