from .models import Deduction
from .forms import DeductionForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

def deduction_list(request):
    deductions = Deduction.objects.all()
    return render(request, 'deductions/list.html', {'deductions': deductions})

def deduction_detail(request, pk):
    deduction = get_object_or_404(Deduction, pk=pk)
    return render(request, 'deductions/detail.html', {'deduction': deduction})

def deduction_create(request):
    if request.method == "POST":
        form = DeductionForm(request.POST)
        if form.is_valid():
            deduction = form.save()
            return redirect('deduction_detail', pk=deduction.pk)
    else:
        form = DeductionForm()
    return render(request, 'deductions/form.html', {'form': form})

def deduction_update(request, pk):
    deduction = get_object_or_404(Deduction, pk=pk)
    if request.method == "POST":
        form = DeductionForm(request.POST, instance=deduction)
        if form.is_valid():
            deduction = form.save()
            return redirect('deduction_detail', pk=deduction.pk)
    else:
        form = DeductionForm(instance=deduction)
    return render(request, 'deductions/form.html', {'form': form})

def deduction_delete(request, pk):
    deduction = get_object_or_404(Deduction, pk=pk)
    if request.method == "POST":
        deduction.delete()
        return redirect('deduction_list')
    return render(request, 'deductions/delete.html', {'deduction': deduction})
