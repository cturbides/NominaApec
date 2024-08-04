from django import forms
from .models import Deduction

class DeductionForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['state', 'name', 'positions', 'depend_on_salary']

        widgets = {
            'positions': forms.CheckboxSelectMultiple,
        }
