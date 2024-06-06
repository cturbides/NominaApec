from django import forms
from .models import Position

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'risk_level', 'minimum_salary', 'maximum_salary']
