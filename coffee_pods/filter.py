import django_filters
from .models import Pods

class PodFilter(django_filters.FilterSet):
    class Meta:
        model = Pods
        fields = '__all__'
        exclude = ['sku']