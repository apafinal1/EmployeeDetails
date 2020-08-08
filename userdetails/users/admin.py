from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'real_name', 'tz', 'start_time', 'end_time']

admin.site.register(Employee, EmployeeAdmin)