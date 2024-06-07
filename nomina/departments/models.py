from django.db import models
from employees.models import Employee

class Department(models.Model):
    id = models.AutoField(verbose_name='department_id', primary_key=True)
    name = models.CharField(verbose_name='department_name', max_length=100)
    physical_ubication = models.CharField(verbose_name='department_physical_ubication', max_length=255)
    area_responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='responsible_departments', verbose_name='area_responsible')

    def __str__(self):
        return self.name
    
