from datetime import datetime
from django.shortcuts import render

def pdf_index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    context = {
        'end_date': today,
    }

    return render(request, 'pdf/index.html', context)
