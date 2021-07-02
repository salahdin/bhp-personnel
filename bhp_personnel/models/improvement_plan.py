from django.db import models

from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from .performance_assessment import PerformanceAssessment


class ImprovementPlan(SiteModelMixin, BaseUuidModel):

    performance_assessment = models.ForeignKey(
        PerformanceAssessment,
        on_delete=models.PROTECT)

    weakness = models.CharField(
        verbose_name='Identified weakness and areas for improvement',
        max_length=150, )

    action_to_take = models.CharField(
        verbose_name='Action Taken/To be taken',
        max_length=200,
        help_text='Coaching, Mentoring, Counselling')

    action_by = models.CharField(
        verbose_name='Action By (Person)',
        max_length=50,)

    review_date = models.DateField()

    completed_date = models.DateField()

    class Meta:
        verbose_name = 'PERFORMANCE IMPROVEMENT PLAN'
        verbose_name_plural = 'PERFORMANCE IMPROVEMENT PLAN'
