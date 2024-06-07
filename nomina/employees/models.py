from django.db import models
from positions.models import Position

class Employee(models.Model):
    id = models.AutoField(verbose_name='employee_id', primary_key=True)
    name = models.CharField(verbose_name='employee_name', max_length=100)
    national_id = models.CharField(verbose_name='national_id', max_length=20, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='position')
    mensual_salary = models.DecimalField(verbose_name='mensual_salary', decimal_places=2, max_digits=11)

    def __str__(self):
        return self.name
