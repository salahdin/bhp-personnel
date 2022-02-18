from django.db import models
from edc_constants.choices import GENDER


class CommonDetailsMixin(models.Model):

    first_name = models.CharField(
        verbose_name="First name",
        max_length=100)

    middle_name = models.CharField(
        verbose_name="Middle names",
        max_length=150,
        blank=True,
        null=True)

    last_name = models.CharField(
        verbose_name="Last name",
        max_length=100)

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        null=True,
        max_length=1)

    email = models.EmailField()

    class Meta:
        abstract = True
