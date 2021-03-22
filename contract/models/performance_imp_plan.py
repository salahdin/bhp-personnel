from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class PerformanceImpPlan(BaseUuidModel, SiteModelMixin):

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
