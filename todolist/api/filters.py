import django_filters
from board.models import AddNote

class AddNoteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # for partial search
    completed = django_filters.BooleanFilter()

    class Meta:
        model = AddNote
        fields = ['title', 'completed']
