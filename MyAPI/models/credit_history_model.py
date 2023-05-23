from django.db import models


class CreditHistory(models.Model):
    client = models.OneToOneField(
        "MyAPI.Approvals", on_delete=models.CASCADE, related_name="credit_history"
    )
    credit_score = models.IntegerField(help_text="Credit score")
    late_payments = models.IntegerField(default=0, help_text="Number of late payments")
    defaults = models.IntegerField(default=0, help_text="Number of defaults")

    def __str__(self):
        return f"Credit History for {self.client.firstname}"