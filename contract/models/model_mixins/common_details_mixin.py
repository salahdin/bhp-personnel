from django.db import models

from edc_base.model_mixins import BaseUuidModel


class CommonDetailsMixin(BaseUuidModel, models.Model):

    first_name = models.CharField(
        verbose_name="First name",
        max_length=50,
        blank=True)

    last_name = models.CharField(
        verbose_name="First name",
        max_length=50,
        blank=True)

    email = models.EmailField()
