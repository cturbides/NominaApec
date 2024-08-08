from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['employee', 'datetime', 'amount', 'income', 'deduction', 'transaction_type', 'state']

        widgets = {
            'income': forms.Select,
            'employee': forms.Select,
            'deduction': forms.Select,
            'amount': forms.NumberInput,
        }
