from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class ResultsFocus(BaseUuidModel, SiteModelMixin):

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

    results_focus_desc = models.CharField(
        verbose_name='Description',
        help_text='',
        max_length=500,
        blank=True,
        null=True)

    results_focus = models.CharField(
        verbose_name='Results Focus and Commitments',
        max_length=500,
        help_text='Refers to the extent to which the employee is self '
                  'motivated to achieve results and continuously strives for '
                  'performance excellence through review and evaluation of '
                  'activities and identification of opportunities for '
                  'improvements and changes to enhance organisational '
                  'efficiencies and success. ')

    results_focus_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Results Focus and Commitments'
        verbose_name_plural = 'Results Focus and Commitments'
