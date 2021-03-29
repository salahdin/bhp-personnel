from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class QualityOfWork(BaseUuidModel, SiteModelMixin):

    emp_identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        null=True,
        blank=True)

    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        blank=True,
        null=True)

    # SECTION 4 – COMPETENCIES AND PROFESSIONAL SKILLS ASSESSMENT

    quality_of_work_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='',
        blank=True,
        null=True)

    quality_of_work = models.IntegerField(
        verbose_name='Quality of Work',
        blank=True,
        null=True,
        help_text='Refers to the extent to which the employee demonstrates '
                  'ability to provide accurate work free of avoidable errors.')

    quality_of_work_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Quality of Work'
        verbose_name_plural = 'Quality of Work'
