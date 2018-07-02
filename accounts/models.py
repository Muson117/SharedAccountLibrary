from django.db import models


class Employee(models.Model):
    employee_FirstName = models.CharField(max_length=100)
    employee_LastName = models.CharField(max_length=100)
    employee_ShortName = models.CharField(max_length=20)
    employee_PersonalPhone = models.CharField(max_length=100, unique=True)
    
class Account(models.Model):
    account_name = models.CharField(max_length=100)
    account_pass = models.CharField(max_length=100)
    account_taken_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    account_taken_at = models.DateTimeField('Account in use since')
    account_free = models.BooleanField(default=False)
