from django.db import models

from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from .performance_assessment import PerformanceAssessment


class CareerDevelopment(SiteModelMixin, BaseUuidModel):

    performance_assessment = models.ForeignKey(
        PerformanceAssessment,
        on_delete=models.PROTECT)

    training_needs = models.CharField(
        verbose_name='Identified Training Needs',
        max_length=150, )

    agreed_action = models.CharField(
        verbose_name='Agreed Action and Timelines for Review',
        max_length=200)

    review_date = models.DateField()

    completion_date = models.DateField()

    development_comments = models.CharField(
        verbose_name='Career Development Comments',
        max_length=200)

    class Meta:
        verbose_name = 'TRAINING AND CAREER DEVELOPMENT PLAN'
        verbose_name_plural = 'TRAINING AND CAREER DEVELOPMENT PLAN'
