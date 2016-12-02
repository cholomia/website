from django.contrib import admin
from .models import Term, Topic, Lesson, LessonDetail, BodyType, Question, QuestionType, Choice, Assessment, \
    AssessmentChoice, Glossary

# Register your models here.
admin.site.register(Term)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(LessonDetail)
admin.site.register(BodyType)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Choice)
admin.site.register(Assessment)
admin.site.register(AssessmentChoice)
admin.site.register(Glossary)
