from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ()
        widgets = {
            'corporate_name': forms.TextInput(attrs={'class': 'form-control'}),
            'corporate_tax_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00', 'maxlength': '18', 'inputmode': 'numeric'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
