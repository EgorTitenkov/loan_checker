import area as area
from django.db import models

from DjangoAPI.MyAPI.models.choices_models import gender_choices, married_status, graduate_status, self_employed
from DjangoAPI.MyAPI.models.client_status_model import client_status
from DjangoAPI.MyAPI.models.credit_history_model import CreditHistory


class Approvals(models.Model):
    client = models.OneToOneField(
        client_status, on_delete=models.CASCADE, related_name="approvals"
    )
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicantincome = models.IntegerField()
    coapplicatincome = models.IntegerField()
    loanamt = models.IntegerField()
    loanterm = models.IntegerField()
    credithistory = models.OneToOneField(
        CreditHistory, on_delete=models.CASCADE, related_name="approvals"
    )
    gender = models.CharField(max_length=15, choices=gender_choices.choices)
    married = models.CharField(max_length=15, choices=married_status.choices)
    graduatededucation = models.CharField(max_length=15, choices=graduate_status.choices)
    selfemployed = models.CharField(max_length=15, choices=self_employed.choices)
    area = models.CharField(max_length=15, choices=area.choices)

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.firstname