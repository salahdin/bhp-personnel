from django.db import models

from ..choices import CONTRACT_STATUS, CONTRACT_LENGTH
from edc_base.model_validators import datetime_not_future
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class Contract(BaseUuidModel, SiteModelMixin, models.Model):

    identifier = models.CharField(
        verbose_name="Identifier",
        max_length=36,
        null=True,
        blank=True)

    duration = models.CharField(
        verbose_name="Contract Duration",
        max_length=30,
        choices=CONTRACT_LENGTH)

    start_date = models.DateField(
        verbose_name='Contract Start Date',
        help_text='Beginning of New Contract')

    end_date = models.DateField(
        verbose_name='Contract End Date',
        help_text='End Date of Contract')

    status = models.CharField(
        verbose_name='Contract Status',
        max_length=30,
        null=True,
        choices=CONTRACT_STATUS)

    contract_ended = models.BooleanField(
        default=False,
        null=True,
        blank=True)
