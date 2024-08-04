from django.db import models
from utils.state_enum import State
from positions.models import Position

class Deduction(models.Model):
    id = models.AutoField(verbose_name='deduction_id', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='deduction_name', max_length=100)
    positions = models.ManyToManyField(Position, verbose_name='positions')
    depend_on_salary = models.BooleanField(verbose_name='depend_on_salary')
    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.ENABLED,
        verbose_name='deduction_state'
    )

    def __str__(self):
        return self.name;
