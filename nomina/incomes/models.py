from django.db import models
from utils.state_enum import State
from positions.models import Position

class Income(models.Model):
    id = models.AutoField(verbose_name='income_id', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='income_name', max_length=100)
    depend_on_salary = models.BooleanField(verbose_name='depend_on_salary')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='position')
    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.ENABLED,
        verbose_name='income_state'
    )

    def __str__(self):
        return self.name
    