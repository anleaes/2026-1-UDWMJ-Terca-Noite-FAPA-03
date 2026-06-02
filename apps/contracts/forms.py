from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    signing_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
            format='%Y-%m-%d',
        ),
        input_formats=['%Y-%m-%d'],
        label='Data de assinatura',
    )

    class Meta:
        model = Contract
        fields = ['number', 'signing_date', 'value', 'validity_days', 'document', 'is_active', 'company']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número do contrato'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Valor'}),
            'validity_days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dias de validade'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'number': 'Número',
            'signing_date': 'Data de assinatura',
            'value': 'Valor',
            'validity_days': 'Dias de validade',
            'document': 'Documento',
            'is_active': 'Ativo',
            'company': 'Empresa',
        }
