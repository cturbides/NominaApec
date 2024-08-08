from django.db import models

class TransactionType(models.TextChoices):
    INCOME = 'Ingreso', 'Income'
    DEDUCTION = 'Deducción', 'Deduction'
