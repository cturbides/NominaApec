from django.shortcuts import render, get_object_or_404, redirect
from .models import Position
from .forms import PositionForm

def position_list(request):
    positions = Position.objects.all()
    return render(request, 'positions/index.html', {'positions': positions})

def position_detail(request, pk):
    position = get_object_or_404(Position, pk=pk)
    return render(request, 'positions/detail.html', {'position': position})

def position_create(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save()
            return redirect('position_detail', pk=position.pk)
    else:
        form = PositionForm()
    return render(request, 'positions/form.html', {'form': form})

def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            position = form.save()
            return redirect('position_detail', pk=position.pk)
    else:
        form = PositionForm(instance=position)
    return render(request, 'positions/form.html', {'form': form})

def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        position.delete()
        return redirect('position_list')
    return render(request, 'positions/delete.html', {'position': position})
