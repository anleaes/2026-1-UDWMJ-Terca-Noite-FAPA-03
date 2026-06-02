from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    occurred_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Ocorrido em',
    )

    class Meta:
        model = Incident
        exclude = ()
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'severity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'is_resolved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'construction': forms.Select(attrs={'class': 'form-select'}),
            'reported_by': forms.Select(attrs={'class': 'form-select'}),
        }
