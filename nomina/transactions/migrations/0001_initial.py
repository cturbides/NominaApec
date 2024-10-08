# Generated by Django 4.2.14 on 2024-08-08 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0005_employee_department'),
        ('incomes', '0002_remove_income_position_income_positions'),
        ('deductions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='transaction_id')),
                ('datetime', models.DateTimeField(verbose_name='datetime')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='amount')),
                ('transaction_type', models.CharField(choices=[('Ingreso', 'Income'), ('Deducción', 'Deduction')], max_length=20, verbose_name='Tipo de Transacción')),
                ('state', models.CharField(choices=[('Habilitada', 'Enabled'), ('Deshabilitada', 'Disabled')], default='Habilitada', max_length=20, verbose_name='deduction_state')),
                ('deduction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deductions.deduction', verbose_name='deduction')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='employee')),
                ('income', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='incomes.income', verbose_name='income')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
