from . import views
from django.urls import path
from .generate_pdf import generate_payroll_pdf

urlpatterns = [
    path('', views.pdf_index, name='pdf_index'),
    path('generate_payroll_pdf/', generate_payroll_pdf, name='generate_payroll_pdf')
]
