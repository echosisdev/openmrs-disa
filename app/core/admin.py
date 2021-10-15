from django.contrib import admin
from core.models import Laboratorio, CsvFile, ExcelFile


admin.site.register(Laboratorio)
admin.site.register(CsvFile)
admin.site.register(ExcelFile)
