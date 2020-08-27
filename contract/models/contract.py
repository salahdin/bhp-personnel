from django.db import models

from ..choices import CONTRACT_LENGTH
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class Contract(BaseUuidModel, SiteModelMixin, models.Model):

    identifier = models.CharField(
        verbose_name="Identifier",
        max_length=36,
        null=True,
        unique=True)

    duration = models.CharField(
        verbose_name="Contract Duration",
        max_length=30,
        choices=CONTRACT_LENGTH)

    start_date = models.DateTimeField(
        verbose_name='Contract Start Date',
        default=get_utcnow,
        validators=[datetime_not_future, ],
        help_text='Beginning of New Contract')

    end_date = models.DateTimeField(
        verbose_name='Contract End Date',
        default=get_utcnow,
        help_text='End Date of Contract')

    active = models.BooleanField(
        verbose_name='Contract Status',
        help_text='Active or Not',
        default=False)
