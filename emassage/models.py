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
    sequence = models.IntegerField(unique=True)
    coverImage = models.FileField(blank=True, null=True)
    pdf = models.FileField()

    def __str__(self):
        return str(self.id) + ": " + self.title
