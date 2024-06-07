from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from .forms import DepartmentForm

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/detail.html', {'department': department})

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'departments/form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('department_list')
    return render(request, 'departments/delete.html', {'department': department})
