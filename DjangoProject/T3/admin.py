from django.contrib import admin
from .models import user, EmployeeDetails
# Register your models here.

admin.site.register(user)
admin.site.register(EmployeeDetails)