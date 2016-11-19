from django.contrib import admin
from .models import Term, Topic, Lesson, LessonDetail, BodyType

# Register your models here.
admin.site.register(Term)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(LessonDetail)
admin.site.register(BodyType)
