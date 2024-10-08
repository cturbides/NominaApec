# Generated by Django 5.0.6 on 2024-06-07 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employees", "0004_alter_employee_national_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="department_id"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="department_name"),
                ),
                (
                    "physical_ubication",
                    models.CharField(
                        max_length=255, verbose_name="department_physical_ubication"
                    ),
                ),
                (
                    "area_responsible",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="responsible_departments",
                        to="employees.employee",
                        verbose_name="area_responsible",
                    ),
                ),
            ],
        ),
    ]
