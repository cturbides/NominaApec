from django.db import models

class State(models.TextChoices):
    ENABLED = 'Habilitada', 'Enabled'
    DISABLED = 'Deshabilitada', 'Disabled'