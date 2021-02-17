from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class PerformanceImpPlan(BaseUuidModel, SiteModelMixin):

    identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        null=True,
        blank=True)

    period = models.CharField(
        verbose_name='Period',
        max_length=50)

    date = models.DateField(
        verbose_name='Date',
        blank=True,
        null=True)

    appraiser = models.CharField(
        verbose_name='Appraiser\'s name',
        max_length=70)

    employee_signature = models.CharField(
        verbose_name='Employee\'s Signature',
        max_length=20)

    supervisor_signature = models.CharField(
        verbose_name='Supervisor\'s Signature',
        max_length=20)

    employee_comments = models.TextField(
        verbose_name='Employee\'s comments',
        max_length=100)

    class Meta:
        verbose_name = 'Performance Improvement Plan'
        verbose_name_plural = 'Performance Improvement Plan'


class ImprovementObjectives(SiteModelMixin, BaseUuidModel):

    performance_imp_plan = models.ForeignKey(
        PerformanceImpPlan,
        on_delete=models.PROTECT)

    effectiveness_area = models.CharField(
        verbose_name='Effectiveness Area (EA) or Objective',
        max_length=200, )

    measures = models.CharField(
        verbose_name='KPIs/Measures',
        max_length=150)

    threshold_target = models.CharField(
        verbose_name='Threshold Target',
        max_length=150)

    stretch_target = models.IntegerField(
        verbose_name='Stretch Target')

    actual_result = models.IntegerField(
        verbose_name='Stretch Target')

    self_score = models.IntegerField(
        verbose_name='Self Score')

    score_by_supervisor = models.IntegerField(
        verbose_name='Score by Supervisor')

    agreed_score = models.IntegerField(
        verbose_name='Agreed Score')

    supervisor_comments = models.CharField(
        verbose_name='Comments by Supervisor',
        max_length=150)

    class Meta:
        verbose_name = 'PERFORMANCE IMPROVEMENT OBJECTIVES'
        verbose_name_plural = 'PERFORMANCE IMPROVEMENT OBJECTIVES'
