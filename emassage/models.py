from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    sequence = models.IntegerField()
    coverImage = models.FileField()

    def __str__(self):
        return self.title
