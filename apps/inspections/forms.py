from django import forms
from .models import Inspection


class InspectionForm(forms.ModelForm):
    visit_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Data da visita',
    )

    class Meta:
        model = Inspection
        fields = ['visit_date', 'status_found', 'description', 'is_compliant', 'score', 'employee']
        widgets = {
            'status_found': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_compliant': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
            'employee': forms.Select(attrs={'class': 'form-select'}),
        }
