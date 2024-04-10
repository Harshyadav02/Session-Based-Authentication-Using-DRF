from django.contrib import admin

from session_api.models import Employee

class EmployeeAdmin(admin.ModelAdmin) :

    list_display = ['employee_id','employee_name','employee_age','employee_salary',]

admin.site.register(Employee,EmployeeAdmin)
