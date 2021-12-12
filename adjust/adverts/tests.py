import decimal

from django.db import connection
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from adverts import factories


class Tests(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        # generate 500 random records
        for i in range(500):
            factories.PerformanceBaseFactory()

    def test_case_1(self):
        factories.PerformanceBaseFactory(date='2017-05-01')
        factories.PerformanceBaseFactory(date='2017-05-05')
        factories.PerformanceBaseFactory(date='2017-05-12')
        factories.PerformanceBaseFactory(date='2017-05-28')
        factories.PerformanceBaseFactory(date='2017-05-30')

        cursor = connection.cursor()
        query = "select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from advertisement_appperformance where date < '2017-06-01' group by channel, country order by clicks desc;"
        cursor.execute(query)

        query_result = [dict(zip(['channel', 'country', 'impressions', 'clicks'], data)) for data in cursor.fetchall()]

        response = self.client.get(f"{reverse('adverts_api:app_performance-list')}?date_to=2017-05-31&group_by"
                                   f"=channel,country&fields=channel,country,impressions,clicks&ordering=-clicks")
        api_result = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(query_result, api_result)

    def test_case_2(self):
        factories.PerformanceBaseFactory(date='2017-05-01', os='ios')
        factories.PerformanceBaseFactory(date='2017-05-05', os='android')
        factories.PerformanceBaseFactory(date='2017-05-12', os='android')
        factories.PerformanceBaseFactory(date='2017-05-28', os='ios')
        factories.PerformanceBaseFactory(date='2017-05-30', os='ios')

        cursor = connection.cursor()
        query = "select date, Sum(installs) as installs from adverts_appperformance where date between '2017-05-01' and'2017-05-31' and os='ios' group by date order by date desc;"
        cursor.execute(query)

        query_result = [dict(zip(['date', 'installs'], [str(data[0]), data[1]])) for data in cursor.fetchall()]

        response = self.client.get(f"{reverse('adverts_api:app_performance-list')}?date_from=2017-05-01&date_to"
                                   f"=2017-05-31&os=ios&group_by=date&ordering=-date&fields=date,installs")
        api_result = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(query_result, api_result)

    def test_case_3(self):
        for i in range(100):
            factories.PerformanceBaseFactory(date='2017-06-01', country='US')

        cursor = connection.cursor()
        query = "select os, Sum(revenue) as revenue from adverts_appperformance where country='US' and date='2017-06-01' group by os order by revenue desc;"
        cursor.execute(query)

        query_result = [dict(zip(['os', 'revenue'], [data[0], round(decimal.Decimal(data[1]), 2)])) for data in cursor.fetchall()]

        response = self.client.get(f"{reverse('adverts_api:app_performance-list')}?date=2017-06-01&country=US"
                                   f"&group_by=os&ordering=-revenue&fields=os,revenue")
        api_result = response.json()['results']
        for data in api_result:
            data['revenue'] = round(decimal.Decimal(data['revenue']), 2)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(query_result, api_result)

    def test_case_4(self):
        cursor = connection.cursor()
        query = "select channel, sum(spend), sum(spend)/sum(installs) as cpi from adverts_appperformance where country='CA' group by channel order by -cpi;"
        cursor.execute(query)
        query_result = [dict(zip(['channel', 'spend', 'cpi'], [data[0], round(decimal.Decimal(data[1]), 2), round(decimal.Decimal(data[2]), 2)])) for data in cursor.fetchall()]

        response = self.client.get(f"{reverse('adverts_api:app_performance-list')}?country=CA&group_by=channel"
                                   f"&ordering=-cpi&fields=channel,spend,cpi")
        api_result = response.json()['results']
        for data in api_result:
            data['spend'] = round(decimal.Decimal(data['spend']), 2)
            data['cpi'] = round(decimal.Decimal(data['cpi']), 2)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(query_result, api_result)
