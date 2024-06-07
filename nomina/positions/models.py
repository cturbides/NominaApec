from django.db import models
from django.core.exceptions import ValidationError

class Position(models.Model):
    id = models.AutoField(verbose_name='position_id', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='position_name', max_length=100)
    risk_level = models.SmallIntegerField(verbose_name='position_risk_level')
    minimum_salary = models.DecimalField(verbose_name='position_minimum_salary', decimal_places=2, max_digits=11)
    maximum_salary = models.DecimalField(verbose_name='position_maximum_salary', decimal_places=2, max_digits=11)

    def clean(self):
        super().clean()
        if self.minimum_salary >= self.maximum_salary:
            raise ValidationError({
                'minimum_salary': 'Minimum salary must be less than maximum salary.',
                'maximum_salary': 'Maximum salary must be greater than minimum salary.',
            })

    def __str__(self):
        return self.name
