from django.urls import path, include
from rest_framework import routers

from adverts.api import views

app_name = "adverts_api"

router = routers.DefaultRouter()
router.register(r"app_performances", views.PerformanceBaseViewSet, basename='app_performance')

urlpatterns = [
    path("", include(router.urls)),
]
