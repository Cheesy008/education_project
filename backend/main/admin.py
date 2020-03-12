from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import nested_admin

from .models import (
    Quiz,
    Question,
    Answer,
)


UserAdmin.fieldsets += ('Custom fields set', {'fields': ('age', 'role')}),


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline, ]


@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'owner',]
    inlines = [QuestionInline, ]


