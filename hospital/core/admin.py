from django.contrib import admin

# Register your models here.
from hospital.core.models import hospitals, normal_bed, icu_bed, ventilators, OxygenCylinders, discharge, \
    death, focalperson, HduBeds

admin.site.register(hospitals)
admin.site.register(normal_bed)
admin.site.register(icu_bed)
admin.site.register(HduBeds)
admin.site.register(ventilators)
admin.site.register(OxygenCylinders)
admin.site.register(discharge)
admin.site.register(death)
admin.site.register(focalperson)
