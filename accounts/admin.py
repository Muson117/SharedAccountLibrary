''' models registered to Django admin interface '''
from django.contrib import admin

# Register your models here.
from .models import Employee, Account

admin.site.register(Employee)
admin.site.register(Account)
