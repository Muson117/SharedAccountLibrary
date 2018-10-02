''' models registered to Django admin interface '''
from django.contrib import admin

# Register your models here.
from .models import Account #,Employee

#admin.site.register(Employee)
#admin.site.register(Account)

admin.site.site_header = "Online Library/Training logins";
admin.site.site_title = "Šaknys Karčios";

'''
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ' what to display in admin '
    list_display = ('employee_FirstName', 'employee_LastName')
'''

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ''' what to display in admin '''
    list_display = ('account_name', 'type', 'status', 'account_taken_by', 'account_taken_at')
    list_filter = ['status', 'type', 'account_taken_at']
    exclude = ['account_pass']

    fieldsets = (
        (None, {
            'fields': ('account_name','type')
        }),
        ('Availability', {
            'fields': ('status', 'account_taken_by',)
        }),
    )

