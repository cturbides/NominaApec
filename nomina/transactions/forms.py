from django import forms
from .models import Transaction
from django.utils import timezone

class TransactionForm(forms.ModelForm):
    datetime = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Transaction
        fields = ['employee', 'datetime', 'amount', 'income', 'deduction', 'state']

        widgets = {
            'income': forms.Select,
            'employee': forms.Select,
            'deduction': forms.Select,
            'amount': forms.NumberInput,
        }
