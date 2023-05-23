from django.db import models

from MyAPI.models.approvals_model import Approvals


class Debt(models.Model):
    approvals = models.OneToOneField(
        Approvals, on_delete=models.CASCADE, related_name="debt"
    )
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Debt for {self.approvals.firstname}"