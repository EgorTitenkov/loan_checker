from django.db import models
from django.utils.translation import gettext_lazy as _


class graduate_status(models.TextChoices):
    Approved = "approved", _("approved")
    Rejected = "rejected", _("rejected")


class married_status(models.TextChoices):
    Married = 'married', _("married")
    Not_Married = 'not_married', _("not_married")


class gender_choices(models.TextChoices):
    Male = "male", _("male")
    Female = "female", _("female")


class self_employed(models.TextChoices):
    Self_Employed = "self employed", _("self employed")
    Not_Self_Employed = "not self employed", _("not self employed")


class area(models.TextChoices):
    Belarus = "Belarus", _("Belarus")
    Russia = "Russia", _("Russia")
    USA = 'USA', _('USA')


class status_choices(models.TextChoices):
    Belarus = "Belarus"
    Russia = "Russia"
    USA = 'USA'


class married_status(models.TextChoices):
    Approve = 'approved'
    Reject = 'rejected'