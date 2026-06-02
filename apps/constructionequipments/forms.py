from django import forms
from .models import ConstructionEquipment


class ConstructionEquipmentForm(forms.ModelForm):
    allocation_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
            format='%Y-%m-%d',
        ),
        input_formats=['%Y-%m-%d'],
        label='Data de alocação',
    )
    
    return_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
            format='%Y-%m-%d',
        ),
        input_formats=['%Y-%m-%d'],
        label='Data de devolução',
        required=False,
    )

    class Meta:
        model = ConstructionEquipment
        exclude = ('construction', 'usage_cost')
        widgets = {
            'equipment': forms.Select(attrs={'class': 'form-select'}),
        }
