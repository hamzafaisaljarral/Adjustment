from rest_framework import serializers

from adverts.api.mixins import QueryFieldsMixin
from adverts.models import PerformanceMeasure


class PerformanceBaseSerializer(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = PerformanceMeasure
        fields = (
            'id',
            'date',
            'channel',
            'country',
            'os',
            'impressions',
            'clicks',
            'installs',
            'spend',
            'revenue',
            'cpi'
        )
