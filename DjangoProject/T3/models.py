from django.db import models

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.user_name
    
class EmployeeDetails(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=20)
    EmployeeDepartment = models.CharField(max_length=20, blank=True, null=True)
    Country = models.CharField(max_length=20, blank=True, null=True)
    Salary = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.EmployeeName
    