from django.db import models

from django_crypto_fields.fields import EncryptedCharField
from edc_constants.choices import GENDER
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import CellNumber


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

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        null=True,
        max_length=1)

    hired_date = models.DateField(
        verbose_name='Hired Date')

    cell = EncryptedCharField(
        verbose_name='Cell number',
        validators=[CellNumber, ],
        blank=False,
        unique=True)

    email = models.EmailField()
