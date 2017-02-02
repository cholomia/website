from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    sequence = models.IntegerField(unique=True)
    coverImage = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    course = models.ForeignKey(Course, related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    sequence = models.IntegerField(unique=True)
    coverImage = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ": " + self.title


class Lesson(models.Model):
    category = models.ForeignKey(Category, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    objective = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(unique=True)
    coverImage = models.FileField(blank=True, null=True)
    pdf = models.FileField()

    def __str__(self):
        return str(self.id) + ": " + self.title


class MobileId(models.Model):
    user = models.ForeignKey('auth.User', related_name='tokens', on_delete=models.CASCADE)
    token = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username + " : " + self.token


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    body = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return str(self.id) + ": Lesson #" + str(self.lesson.id) + " " + self.body


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.id) + ": Question #" + str(self.question.id) + " " + self.body


class Forum(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    user = models.ForeignKey('auth.User', related_name='forums', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    forum = models.ForeignKey(Forum, related_name='forum_comments', on_delete=models.CASCADE)
    body = models.TextField()
    user = models.ForeignKey('auth.User', related_name='user_comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.forum.title + ": " + self.body

    class Meta:
        ordering = ('-created',)


class Grade(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    lesson = models.ForeignKey(Lesson, related_name='grades', on_delete=models.CASCADE)
    raw_score = models.IntegerField()
    item_count = models.IntegerField()
    user = models.ForeignKey('auth.User', related_name='user_grades', on_delete=models.CASCADE)
    try_count = models.IntegerField()

    def __str__(self):
        return self.id


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    validation_code = models.CharField(max_length=100)
    enable = models.BooleanField()

    def __str__(self):
        return self.user.username


class ForumVote(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    forum = models.ForeignKey(Forum, related_name='forum_votes', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_forum_votes', on_delete=models.CASCADE)
    vote = models.IntegerField()

    def __str__(self):
        return self.id


class CommentVote(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    comment = models.ForeignKey(Comment, related_name='comment_votes', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_comment_votes', on_delete=models.CASCADE)
    vote = models.IntegerField()

    def __str__(self):
        return self.id


class VideoSimulation(models.Model):
    youtube_code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TwistWord(models.Model):
    word = models.CharField(max_length=50)
    clue = models.TextField()

    def __str__(self):
        return self.word
