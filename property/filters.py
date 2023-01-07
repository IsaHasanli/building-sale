import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    area = django_filters.RangeFilter()
    price = django_filters.RangeFilter()
    class Meta:
        model = Property
        fields = ['location','category', 'building_type', 'property_type', 'price', 'area' ]