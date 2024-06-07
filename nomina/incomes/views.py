from django.shortcuts import render, get_object_or_404, redirect
from .models import Income
from .forms import IncomeForm

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'incomes/list.html', {'incomes': incomes})

def income_detail(request, pk):
    income = get_object_or_404(Income, pk=pk)
    return render(request, 'incomes/detail.html', {'income': income})

def income_create(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save()
            return redirect('income_detail', pk=income.pk)
    else:
        form = IncomeForm()
    return render(request, 'incomes/form.html', {'form': form})

def income_update(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save()
            return redirect('income_detail', pk=income.pk)
    else:
        form = IncomeForm(instance=income)
    return render(request, 'incomes/form.html', {'form': form})

def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        income.delete()
        return redirect('income_list')
    return render(request, 'incomes/delete.html', {'income': income})
