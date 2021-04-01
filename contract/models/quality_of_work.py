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
        help_text='<p>Refers to the extent to which the employee demonstrates '
                  'ability to provide accurate work free of avoidable errors.'
                  'Perfcormance indicators include :<br></p>'
                  '<p>&#10003;Demonstrates attention to detail, '
                  'checks work thoroughly and rarely submits work with obvious'
                  ' errors<br>'
                  '&#10003;Follows up any work quality queries promptly and '
                  'makes required adjustments accurately to avoid further '
                  'delays<br>'
                  '&#10003;Quality checks others’ work and provides relevant '
                  'feedback for quality team deliverables<br></p>',
        blank=True,
        null=True)

    quality_of_work = models.IntegerField(
        verbose_name='Quality of Work',
        blank=True,
        null=True,)

    quality_of_work_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Quality of Work'
        verbose_name_plural = 'Quality of Work'
