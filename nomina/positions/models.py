from django.db import models

class Position(models.Model):
    id = models.AutoField(verbose_name='position_id', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='position_name', max_length=100)
    riskLevel = models.SmallIntegerField(verbose_name='position_risk_level')
    minimumSalary = models.DecimalField(verbose_name='position_minimum_salary', decimal_places=2, max_digits=11)
    maximumSalary = models.DecimalField(verbose_name='position_maximum_salary', decimal_places=2, max_digits=11)

    def __str__(self):
        return self.name
