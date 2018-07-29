''' models registered to Django admin interface '''
from django.contrib import admin

# Register your models here.
from .models import Employee, Account

#admin.site.register(Employee)
#admin.site.register(Account)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ''' what to display in admin '''
    list_display = ('employee_FirstName', 'employee_LastName')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ''' what to display in admin '''
    #list_filter = ("account_status")
