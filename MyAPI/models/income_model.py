from django.db import models

from MyAPI.models.approvals_model import Approvals


class Income(models.Model):
    approvals = models.OneToOneField(
        Approvals, on_delete=models.CASCADE, related_name="income"
    )
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Income for {self.approvals.firstname}"