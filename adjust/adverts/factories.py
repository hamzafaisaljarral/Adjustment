import datetime

import factory
from factory import fuzzy

from adverts.models import PerformanceMeasure


class PerformanceBaseFactory(factory.django.DjangoModelFactory):
    date = fuzzy.FuzzyDate(datetime.date(2000, 1, 1))
    channel = fuzzy.FuzzyChoice(['adcolony', 'apple_search_ads', 'chartboost', 'facebook', 'google', 'unityads', 'vungle'])
    country = fuzzy.FuzzyChoice(['US', 'DE', 'GB', 'CA', 'FR'])
    os = fuzzy.FuzzyChoice(['android', 'ios'])
    impressions = fuzzy.FuzzyInteger(27441)
    clicks = fuzzy.FuzzyInteger(1000)
    installs = fuzzy.FuzzyInteger(200)
    spend = fuzzy.FuzzyDecimal(50000)
    revenue = fuzzy.FuzzyDecimal(2000)

    class Meta:
        model = PerformanceMeasure
