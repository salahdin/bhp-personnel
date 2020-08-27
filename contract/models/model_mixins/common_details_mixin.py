from django.db import models

from edc_base.model_mixins import BaseUuidModel


class CommonDetailsMixin(BaseUuidModel, models.Model):

    first_name = models.CharField(
        verbose_name="First name",
        max_length=100)
    
    middle_name = models.CharField(
        verbose_name="Middle names",
        max_length=150,
        blank=True)

    last_name = models.CharField(
        verbose_name="Last name",
        max_length=100)

    email = models.EmailField()
