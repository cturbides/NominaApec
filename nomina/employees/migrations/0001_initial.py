# Generated by Django 5.0.6 on 2024-06-07 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("positions", "0003_rename_maximumsalary_position_maximum_salary_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="employee_id"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="employee_name"),
                ),
                (
                    "national_id",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="national_id"
                    ),
                ),
                (
                    "mensual_salary",
                    models.DecimalField(
                        decimal_places=2, max_digits=11, verbose_name="mensual_salary"
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="positions.position",
                        verbose_name="position",
                    ),
                ),
            ],
        ),
    ]
