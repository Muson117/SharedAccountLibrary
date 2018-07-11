from django.db import models


class Employee(models.Model):
    employee_FirstName = models.CharField(max_length=100)
    employee_LastName = models.CharField(max_length=100)
    employee_ShortName = models.CharField(max_length=20)
    employee_PersonalPhone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.employee_FirstName +'_'+ self.employee_LastName
    
class Account(models.Model):
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
        return self.account_name

    def is_free(self):
        return self.account_free == True
        

