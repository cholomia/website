from django.contrib import admin
from emassage.models import Course, Category, Lesson, MobileId, Question, Choice, Forum, Comment, Grade, UserProfile, \
    ForumVote, CommentVote, VideoSimulation

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(MobileId)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Grade)
admin.site.register(UserProfile)
admin.site.register(ForumVote)
admin.site.register(CommentVote)
admin.site.register(VideoSimulation)
