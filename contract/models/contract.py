from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


from ..choices import CONTRACT_STATUS, CONTRACT_LENGTH


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


class ContractExtension(BaseUuidModel):

    contract = models.ForeignKey(Contract, on_delete=PROTECT)

    ext_duration = models.IntegerField(
        verbose_name='Extension time period (in months)',)

    end_date = models.DateField(
        verbose_name='New Contract End Date',
        help_text='End Date of contract after extension', )

    def save(self, *args, **kwargs):
        self.end_date = self.contract.end_date + relativedelta(
            months=self.ext_duration)
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Contract Extension'
        verbose_name_plural = 'Contract Extension'
