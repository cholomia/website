from django.db import models


# Create your models here.
class BodyType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Term(models.Model):
    code = models.CharField(max_length=2)
    title = models.CharField(max_length=250)
    objective = models.CharField(max_length=1000)
    sequence = models.IntegerField()

    def __str__(self):
        return self.title


class Topic(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    objective = models.CharField(max_length=1000)
    image = models.CharField(max_length=250)


class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)


class LessonDetail(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    body = models.TextField()
    caption = models.CharField(max_length=1000)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
