from django.contrib import admin
import nested_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Profile

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', ]


class QuizInline(nested_admin.NestedTabularInline):
    model = Profile.quiz.through


@admin.register(Profile)
class ProfileAdmin(nested_admin.NestedModelAdmin):

    exclude = ['quiz', ]
    inlines = [QuizInline, ]


