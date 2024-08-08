from django.db import models
from incomes.models import Income
from utils.state_enum import State
from employees.models import Employee
from deductions.models import Deduction
from django.core.exceptions import ValidationError
from utils.transaction_type_enum import TransactionType
from utils.constants import MAX_DIGITS_OF_TRANSACTION_AMOUNT, MAX_DECIMALS_OF_TRANSACTION_AMOUNT

class Transaction(models.Model):
    id = models.AutoField(verbose_name='transaction_id', auto_created=True, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='employee')
    datetime = models.DateTimeField(verbose_name='datetime')
    amount = models.DecimalField(max_digits=MAX_DIGITS_OF_TRANSACTION_AMOUNT, decimal_places=MAX_DECIMALS_OF_TRANSACTION_AMOUNT, verbose_name='amount')
    income = models.ForeignKey(Income, null=True, blank=True, on_delete=models.CASCADE, verbose_name='income')
    deduction = models.ForeignKey(Deduction, null=True, blank=True, on_delete=models.CASCADE, verbose_name='deduction')
    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionType.choices,
        verbose_name='Tipo de Transacción'
    )
    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.ENABLED,
        verbose_name='deduction_state'
    )

    def clean(self):
        if not self.income and not self.deduction:
            raise ValidationError('Debe especificar un income o una deduction.')
        if self.income and self.deduction:
            raise ValidationError('No puede especificar ambos: income y deduction.')

        if self.income:
            self.transaction_type = TransactionType.INCOME
        elif self.deduction:
            self.transaction_type = TransactionType.DEDUCTION
        else:
            raise ValidationError('Se debe especificar: income y deduction.')

    def __str__(self):
        amount_formatted = f'{self.amount:,.2f}$'
        description = self.income.name if self.income else self.deduction.name
        employee_name = self.employee.name
        return f'{amount_formatted} - {description} - {employee_name}'

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
