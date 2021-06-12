from django.contrib import admin

# Register your models here.


from hospital.commons.models import Corona, contact


admin.site.register(Corona)
admin.site.register(contact)


