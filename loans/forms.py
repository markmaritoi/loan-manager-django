from django import forms
from .models import Loan, Repayment

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['lender_name', 'borrower_name', 'original_amount', 'reason']
        widgets = {
            'lender_name': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name': forms.TextInput(attrs={'class': 'form-control'}),
            'original_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RepaymentForm(forms.ModelForm):
    class Meta:
        model = Repayment
        fields = ['amount', 'payment_method', 'note']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }