from django.contrib import admin

# Register your models here.
from hospital.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)
    search_fields = ('email', 'first_name', 'last_name', 'hospital')
