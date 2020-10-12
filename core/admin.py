from django.contrib import admin
from .models import PontoTuristico


admin.site.site_header = "Dandy Administration"
admin.site.register(PontoTuristico)