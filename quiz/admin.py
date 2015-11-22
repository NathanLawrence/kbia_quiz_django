from django.contrib import admin
from .models import Quiz, Question, Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'text', 'order']
    list_filter = ['quiz']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)