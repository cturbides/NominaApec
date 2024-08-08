from .models import Transaction
from .forms import TransactionForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/list.html', {'transactions': transactions})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transactions/detail.html', {'transaction': transaction})

def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()
    return render(request, 'transactions/form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/delete.html', {'transaction': transaction})
