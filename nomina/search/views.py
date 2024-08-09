from django.db.models import Q
from django.urls import reverse
from incomes.models import Income
from django.shortcuts import render
from django.http import JsonResponse
from positions.models import Position
from employees.models import Employee
from deductions.models import Deduction
from departments.models import Department

def search(request):
    get_options_url = reverse('get_options')
    return render(request, 'search/index.html', {'get_options_url': get_options_url})

def search_result(request):
    show_related = request.GET.get('show_related') == 'on'
    show_transactions = request.GET.get('show_transactions') == 'on'

    employee_results = Employee.objects.all()
    department_results = Department.objects.all()
    position_results = Position.objects.all()
    deduction_results = Deduction.objects.all()
    income_results = Income.objects.all()

    for key, value in request.GET.items():
        if key.startswith('entity_') and value:
            value_key = key.replace('entity', 'value')
            entity = request.GET.get(key)
            entity_value = request.GET.get(value_key)

            if entity == 'employee':
                employee_results = employee_results.filter(pk=entity_value)
                if show_related:
                    department_results = department_results.filter(employee__pk=entity_value)
                    position_results = position_results.filter(employee__pk=entity_value)
                    deduction_results = deduction_results.filter(employee__pk=entity_value)
                    income_results = income_results.filter(employee__pk=entity_value)
            elif entity == 'department':
                department_results = department_results.filter(pk=entity_value)
                if show_related:
                    employee_results = employee_results.filter(department__pk=entity_value)
                    position_results = position_results.filter(department__pk=entity_value)
                    deduction_results = deduction_results.filter(department__pk=entity_value)
                    income_results = income_results.filter(department__pk=entity_value)
            elif entity == 'position':
                position_results = position_results.filter(pk=entity_value)
                if show_related:
                    employee_results = employee_results.filter(position__pk=entity_value)
                    department_results = department_results.filter(position__pk=entity_value)
                    deduction_results = deduction_results.filter(position__pk=entity_value)
                    income_results = income_results.filter(position__pk=entity_value)
            elif entity == 'deduction':
                deduction_results = deduction_results.filter(pk=entity_value)
                if show_related:
                    employee_results = employee_results.filter(deduction__pk=entity_value)
                    department_results = department_results.filter(deduction__pk=entity_value)
                    position_results = position_results.filter(deduction__pk=entity_value)
                    income_results = income_results.filter(deduction__pk=entity_value)
            elif entity == 'income':
                income_results = income_results.filter(pk=entity_value)
                if show_related:
                    employee_results = employee_results.filter(income__pk=entity_value)
                    department_results = department_results.filter(income__pk=entity_value)
                    position_results = position_results.filter(income__pk=entity_value)
                    deduction_results = deduction_results.filter(income__pk=entity_value)

    context = {
        'show_transactions': show_transactions,
        'income_results': income_results.distinct(),
        'employee_results': employee_results.distinct(),
        'position_results': position_results.distinct(),
        'deduction_results': deduction_results.distinct(),
        'department_results': department_results.distinct(),
    }

    return render(request, 'search/search_results.html', context)

def get_options(request):
    entity = request.GET.get('entity')
    options = []

    if entity == 'employee':
        options = [{'value': employee.pk, 'label': employee.name} for employee in Employee.objects.all()]
    elif entity == 'department':
        options = [{'value': department.pk, 'label': department.name} for department in Department.objects.all()]
    elif entity == 'position':
        options = [{'value': position.pk, 'label': position.name} for position in Position.objects.all()]
    elif entity == 'income':
        options = [{'value': income.pk, 'label': income.name} for income in Income.objects.all()]
    elif entity == 'deduction':
        options = [{'value': deduction.pk, 'label': deduction.name} for deduction in Deduction.objects.all()]

    return JsonResponse({'options': options})
