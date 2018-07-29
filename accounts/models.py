''' models for accounts app '''
from django.db import models


class Employee(models.Model):
    ''' holds users '''
    employee_FirstName = models.CharField("FirstName", max_length=100)
    employee_LastName = models.CharField("LastName", max_length=100)
    employee_ShortName = models.CharField(max_length=20, help_text="Your BB number", blank=True)
    employee_PersonalPhone = models.CharField(max_length=100, unique=True)
    employee_PersonalEmail = models.EmailField(unique=True, blank=True, null=True,)

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
    #account_free = models.BooleanField(default=True)
    account_status_options = (
        ('t', 'Taken'),
        ('a', 'Available'),
        ('m', 'Maintenance'),
    )

    account_status = models.CharField(
        max_length=1,
        choices=account_status_options,
        blank=True,
        default='m',
        help_text='Account availability',
    )

    #class Meta:
    #    ordering = ["account_status", "-account_taken_at"]

    def __str__(self):
        ''' return account name '''
        return self.account_name
