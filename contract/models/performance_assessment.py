from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class PerformanceAssessment(BaseUuidModel, SiteModelMixin):

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

    review = models.CharField(
        max_length=50,
        blank=True,
        null=True)

    agreed_by = models.CharField(
        verbose_name='Agreed By',
        max_length=30)

    supervisor_signature = models.CharField(
        max_length=25
    )

    date_supervisor_signed = models.DateField(blank=True, null=True)

    employee_signature = models.CharField(
        max_length=25
    )

    date_employee_signed = models.DateField(blank=True, null=True)

    date = models.DateField(blank=True, null=True)

    overall_perf_score = models.IntegerField(
        verbose_name='Overall Performance Score',
        blank=True,
        null=True)

    comp_nd_pro_score = models.IntegerField(
        verbose_name='Overall Competencies & Professional Skills Score',
        blank=True,
        null=True)

    final_assess_score = models.IntegerField(
        verbose_name='Final Assessment Score (Add the weighted scores)',
        blank=True,
        null=True)

    total_performance_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.emp_identifier}'

    class Meta:
        app_label = 'contract'
        verbose_name = 'Performance Assessment'
        verbose_name_plural = 'Performance Assessment'
