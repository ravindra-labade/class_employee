from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "emp_id": forms.NumberInput(attrs={'class': 'form-control'}),
            "emp_name": forms.TextInput(attrs={'class': 'form-control'}),
            "emp_sal": forms.NumberInput(attrs={'class': 'form-control'}),
            "company_name": forms.TextInput(attrs={'class': 'form-control'}),
            "work_mode": forms.Select(attrs={'class': 'form-control'}),
        }
