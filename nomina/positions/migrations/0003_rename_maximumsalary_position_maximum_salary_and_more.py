# Generated by Django 5.0.6 on 2024-06-06 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("positions", "0002_alter_position_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="position",
            old_name="maximumSalary",
            new_name="maximum_salary",
        ),
        migrations.RenameField(
            model_name="position",
            old_name="minimumSalary",
            new_name="minimum_salary",
        ),
        migrations.RenameField(
            model_name="position",
            old_name="riskLevel",
            new_name="risk_level",
        ),
    ]
