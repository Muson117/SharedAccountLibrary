''' models for accounts app '''
from django.db import models


class Employee(models.Model):
    ''' holds users '''
    employee_FirstName = models.CharField(max_length=100)
    employee_LastName = models.CharField(max_length=100)
    employee_ShortName = models.CharField(max_length=20)
    employee_PersonalPhone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.employee_FirstName +'_'+ self.employee_LastName

class Account(models.Model):
    ''' holds login accounts class '''
    account_name = models.CharField(max_length=100)
    account_pass = models.CharField(max_length=100)
    account_taken_by = models.ForeignKey(Employee,
                                         models.SET_NULL,
                                         blank=True,
                                         null=True,
                                        )
    account_taken_at = models.DateTimeField('Account in use since', auto_now=True)
    account_free = models.BooleanField(default=True)

    def __str__(self):
        ''' return account name '''
        return self.account_name

    def is_free(self):
        ''' method to check if account if available '''
        return self.account_free
