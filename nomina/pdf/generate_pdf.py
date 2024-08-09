import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from transactions.models import Transaction

def generate_payroll_pdf(request):
    end_date = request.GET.get('end_date')
    start_date = request.GET.get('start_date')
    include_incomes = request.GET.get('include_incomes') == 'on'
    include_deductions = request.GET.get('include_deductions') == 'on'

    transactions = Transaction.objects.filter(datetime__range=[start_date, end_date])

    incomes = transactions.filter(income__isnull=False) if include_incomes else []
    deductions = transactions.filter(deduction__isnull=False) if include_deductions else []

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)
    p.setTitle("Nómina")

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 750, "Nómina")

    p.setFont("Helvetica", 12)
    p.drawString(50, 720, "Nómina UNAPEC")
    p.drawString(50, 700, f"Período: {start_date} a {end_date}")

    y = 670

    if include_incomes:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y, "Ingresos")
        y -= 20
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y, "Empleado")
        p.drawString(200, y, "Descripción")
        p.drawString(400, y, "Monto")
        y -= 20

        total_incomes = 0
        for transaction in incomes:
            p.drawString(50, y, transaction.employee.name)
            p.drawString(200, y, transaction.income.name)
            p.drawString(400, y, f"{transaction.amount:,.2f}$")
            total_incomes += transaction.amount
            y -= 20

            if y < 100:
                p.showPage()
                y = 750

        p.drawString(50, y - 20, "Total Ingresos:")
        p.drawString(400, y - 20, f"{total_incomes:,.2f}$")
        y -= 40

    if include_deductions:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y, "Deducciones")
        y -= 20
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, y, "Empleado")
        p.drawString(200, y, "Descripción")
        p.drawString(400, y, "Monto")
        y -= 20

        total_deductions = 0
        for transaction in deductions:
            p.drawString(50, y, transaction.employee.name)
            p.drawString(200, y, transaction.deduction.name)
            p.drawString(400, y, f"{transaction.amount:,.2f}$")
            total_deductions += transaction.amount
            y -= 20

            if y < 100:
                p.showPage()
                y = 750

        p.drawString(50, y - 20, "Total Deducciones:")
        p.drawString(400, y - 20, f"{total_deductions:,.2f}$")

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'nomina_from{start_date}_to_{end_date}.pdf')
