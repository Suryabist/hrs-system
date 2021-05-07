from django.contrib import admin

# Register your models here.
from hospital.core.models import hospitals, normal_bed, icu_bed, ventilators, location

admin.site.register(hospitals)
admin.site.register(normal_bed)
admin.site.register(icu_bed)
admin.site.register(ventilators)
admin.site.register(location)
