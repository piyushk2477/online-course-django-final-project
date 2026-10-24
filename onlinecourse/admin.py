from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from .models import Choice, Course, Lesson, Question, Submission


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class QuestionInline(StackedInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('text', 'lesson', 'order')
    list_filter = ('lesson__course',)
    search_fields = ('text',)
    inlines = [ChoiceInline]


@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title',)
    inlines = [QuestionInline]


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = ('lesson', 'user', 'score', 'total_questions', 'submitted_at')
    readonly_fields = ('submitted_at',)

