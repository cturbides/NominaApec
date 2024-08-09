from django.db import models
from positions.models import Position
from .validators import validate_national_id
from django.core.exceptions import ValidationError

class Employee(models.Model):
    id = models.AutoField(verbose_name='employee_id', primary_key=True)
    name = models.CharField(verbose_name='employee_name', max_length=100)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='department')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='position')
    mensual_salary = models.DecimalField(verbose_name='mensual_salary', decimal_places=2, max_digits=11)
    national_id = models.CharField(
        unique=True,
        max_length=12,
        verbose_name='national_id',
        validators=[validate_national_id]
    )

    def clean(self):
        super().clean()
        if self.mensual_salary < self.position.minimum_salary or self.mensual_salary > self.position.maximum_salary:
            raise ValidationError({
                'mensual_salary': f'The monthly salary must be between {self.position.minimum_salary} and {self.position.maximum_salary}.'
            })


    def __str__(self):
        return self.name
