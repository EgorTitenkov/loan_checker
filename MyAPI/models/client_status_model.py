from django.db import models

from MyAPI.models.choices_models import status_choices


class client_status(models.Model):
    id = models.AutoField(primary_key=True)
    loan_status = models.CharField(max_length=10, choices=status_choices.choices)
