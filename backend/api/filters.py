from django_filters import FilterSet
from django_filters import rest_framework as filters


from main.models import Quiz


class QuizFilter(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    username = filters.CharFilter(field_name='owner__username', lookup_expr='icontains')

    class Meta:
        model = Quiz
        fields = ['title', 'username']