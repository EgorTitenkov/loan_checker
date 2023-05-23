from django.db import models

from DjangoAPI.MyAPI.models.approvals_model import Approvals


class TotalDebt(models.Model):
    client = models.OneToOneField(
        Approvals, on_delete=models.CASCADE, related_name="total_debt"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total debt amount")

    def __str__(self):
        return f"Total Debt for {self.client.firstname}"
