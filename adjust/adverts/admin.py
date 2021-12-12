from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from adverts.models import PerformanceMeasure


class PerformanceBaseResource(resources.ModelResource):
    class Meta:
        model = PerformanceMeasure


class PerformanceBaseAdmin(ImportExportModelAdmin):
    resource_class = PerformanceBaseResource


admin.site.register(PerformanceMeasure, PerformanceBaseAdmin)
