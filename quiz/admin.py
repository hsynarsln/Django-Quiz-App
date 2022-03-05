from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import Answers, Category, Question, Quiz


class AnswersInline(SuperInlineModelAdmin, admin.TabularInline):
    model = Answers
    extra = 4


class QuestionInline(SuperInlineModelAdmin, admin.StackedInline):
    model = Question
    extra = 1
    inlines = [AnswersInline]


class QuizAdmin(SuperModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answerText', 'isRight')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'title', 'difficulty')


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)
