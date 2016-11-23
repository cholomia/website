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
    term = models.ForeignKey(Term, related_name='topics', on_delete=models.CASCADE)
    sequence = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    objective = models.CharField(max_length=1000)
    image = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title + " from " + self.term.title


class Lesson(models.Model):
    topic = models.ForeignKey(Topic, related_name='lessons', on_delete=models.CASCADE)
    sequence = models.IntegerField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class LessonDetail(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='lessondetails', on_delete=models.CASCADE)
    sequence = models.IntegerField()
    body = models.TextField()
    caption = models.CharField(max_length=1000, blank=True)
    body_type = models.ForeignKey(BodyType, related_name='bodytype', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ": Lesson Detail #" + str(self.sequence) + " for " + self.lesson.title


class QuestionType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    question_type = models.ForeignKey(QuestionType, related_name='questiontype', on_delete=models.CASCADE)

    def __str__(self):
        return "ID# " + str(self.id) + " Question for " + self.topic.title + ": " + self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_type = models.ForeignKey(BodyType, related_name='choicetype', on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return "ID# " + str(self.id) + " Choice for Question ID# " + str(self.question.id) + ": " + self.body


class Assessment(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    question_type = models.ForeignKey(QuestionType, related_name='assessmenttype', on_delete=models.CASCADE)

    def __str__(self):
        return "ID# " + str(self.id) + ": " + self.question


class AssessmentChoice(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='assessmentchoices', on_delete=models.CASCADE)
    choice_type = models.ForeignKey(BodyType, related_name='assessmentchoicetype', on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return "ID# " + str(self.id) + " Choice for Question ID# " + str(self.assessment.id) + ": " + self.body
