from django import forms
from .models import AuditReport


class AuditReportForm(forms.ModelForm):
    issue_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
            format='%Y-%m-%d',
        ),
        input_formats=['%Y-%m-%d'],
        label='Data de emissão',
    )

    class Meta:
        model = AuditReport
        fields = ['number', 'issue_date', 'conclusion', 'is_approved']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
