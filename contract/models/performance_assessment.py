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

    period_covered = models.CharField(
        verbose_name='Review Dates',
        max_length=200,
        blank=True,
        null=True)

    mid_year_review = models.DateField(blank=True, null=True)

    year_end_review = models.DateField(blank=True, null=True)

    contract_end_review = models.DateField(blank=True, null=True)

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

    approved_by = models.CharField(
        verbose_name='Approved By',
        max_length=200,
        blank=False,
        null=False)

    signature = models.CharField(
        max_length=25)

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

    emp_comments = models.TextField(
        verbose_name='Comments by employee',
        blank=True,
        null=True)

    supervisor_comments = models.TextField(
        verbose_name='Comments by supervisor',
        blank=True,
        null=True)

    emp_name = models.CharField(
        verbose_name='Employee\'s Name',
        max_length=30,)

    manager = models.CharField(
        verbose_name='Manager / Study Coordinator / Director / Executive / '
                     'Head of Department:  ',
        max_length=30,)

    manager_signature = models.CharField(
        verbose_name='Manager\'s signature',
        max_length=35)

    date_manager_signed = models.CharField(
        verbose_name='Date manager signed',
        max_length=35)

    total_performance_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.emp_identifier}'

    class Meta:
        app_label = 'contract'
        verbose_name = 'Performance Assessment'
        verbose_name_plural = 'Performance Assessment'
