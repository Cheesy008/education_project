from django.contrib import admin
import nested_admin

from .models import (
    Quiz,
    Question,
    Answer,
)


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline, ]


@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline, ]


