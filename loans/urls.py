from django.urls import path
from . import views

urlpatterns = [
    path("", views.loan_list, name="loan_list"),
    path("create/", views.create_loan, name="create_loan"),
    path("loan/<int:loan_id>/", views.loan_detail, name="loan_detail"),
    path("repayment/<int:repayment_id>/delete/", views.delete_repayment, name="delete_repayment"),
    path("loan/<int:loan_id>/delete/", views.delete_loan, name="delete_loan")
]