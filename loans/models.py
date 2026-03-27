from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Loan(models.Model):
    lender_name = models.CharField(max_length=150)
    borrower_name = models.CharField(max_length=150)
    original_amount = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.borrower_name} owes {self.lender_name} €{self.original_amount}"

    def total_repaid(self):
        return sum(x.amount for x in self.repayments.all())
    
    def remaining_balance(self):
        return self.original_amount - self.total_repaid()

class Repayment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),
        ('revolut', 'Revolut'),
        ('paypal', 'Paypal'),
    ]

    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="repayments")
    amount = models.PositiveIntegerField()
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    note = models.TextField(blank=True)

    def clean(self):
        if not self.loan_id:
            return

        remaining = self.loan.remaining_balance()

        if self.amount > remaining:
            raise ValidationError(f"Amount can't be more than remaining balance of €{remaining}")

        if self.amount <= 0:
            raise ValidationError("Repayment amount must be greater than 0.")

    def __str__(self):
        return f"€{self.amount} repayment to {self.loan.lender_name}"