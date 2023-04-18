from django_filters import rest_framework as filters
from .models import Work

class WorkFilter(filters.FilterSet):
    work_type = filters.CharFilter(field_name='work_type')
    artist_name = filters.CharFilter(field_name='artists__name')

    class Meta:
        model = Work
        fields = ['work_type', 'artist_name']

