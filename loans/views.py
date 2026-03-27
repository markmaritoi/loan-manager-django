from django.shortcuts import render, get_object_or_404, redirect
from .models import Loan, Repayment
from .forms import LoanForm, RepaymentForm

def loan_list(request):
    loans = Loan.objects.all()
    return render(request, "loan_list.html", {
        "loans": loans
    })

def create_loan(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loan_list")
    else:
        form = LoanForm()

    return render(request, "create_loan.html", {
        "form": form
    })

def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    repayments = loan.repayments.all()

    if loan.original_amount > 0:
        progress_percentage = int((loan.total_repaid() / loan.original_amount) * 100)
    else:
        progress_percentage = 0

    if request.method == "POST":
        form = RepaymentForm(request.POST)
        form.instance.loan = loan

        if form.is_valid():
            form.save()
            return redirect("loan_detail", loan_id=loan.id)
    else:
        form = RepaymentForm()

    return render(request, "loan_detail.html", {
        "loan": loan,
        "repayments": repayments,
        "form": form,
        "progress_percentage": progress_percentage,
    })

def delete_repayment(request, repayment_id):
    repayment = get_object_or_404(Repayment, id=repayment_id)
    loan_id = repayment.loan.id

    if request.method == "POST":
        repayment.delete()
        return redirect("loan_detail", loan_id=loan_id)

    return render(request, "delete_repayment.html", {
        "repayment": repayment
    })

def delete_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)

    if request.method == "POST":
        loan.delete()
        return redirect('loan_list')

    return render(request, 'delete_loan.html', {'loan': loan})