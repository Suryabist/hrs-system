from django.contrib import admin

# Register your models here.
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from hospital.core.models import hospitals, normal_bed, icu_bed, ventilators, OxygenCylinders, discharge, \
    death, focalperson, HduBeds


class HospitalResource(resources.ModelResource):
    capacity = fields.Field(column_name='capacity', attribute='icu_bed',
                              widget=ForeignKeyWidget(icu_bed, 'capacity'))

    class Meta:
        model = hospitals
        fields = ('id', 'name', 'address', 'hospital_type', 'phone_no', 'capacity', )


class Hospitaladmin(ImportExportModelAdmin):
    resource_class = HospitalResource


admin.site.register(hospitals, Hospitaladmin)
admin.site.register(normal_bed)
admin.site.register(icu_bed)
admin.site.register(HduBeds)
admin.site.register(ventilators)
admin.site.register(OxygenCylinders)
admin.site.register(discharge)
admin.site.register(death)
admin.site.register(focalperson)
