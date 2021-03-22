from django.db import models

from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from .performance_assessment import Contract
from ..choices import PERFORMANCE_RATING


class KeyPerformanceArea(SiteModelMixin, BaseUuidModel):

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
        verbose_name = 'Key Performance Areas'
        verbose_name_plural = 'Key Performance Areas'


class KeyPerformanceAreaItem(SiteModelMixin, BaseUuidModel):

    key_performance_area = models.ForeignKey(
        KeyPerformanceArea,
        on_delete=models.PROTECT)

    kpa_nd_objective = models.CharField(
        verbose_name='KEY PERFORMANCE AREA and OBJECTIVES',
        max_length=250, )

    performance_indicators = models.CharField(
        verbose_name='Key PERFORMANCE INDICATORS / MEASURES & DEADLINES '
                     '(completion dates)',
        max_length=150,)

    weighting = models.CharField(
        verbose_name='%WEIGHTING (KPA Weighting as % of total)',
        max_length=50,)

    mid_year_performance = models.CharField(
        verbose_name='Mid-Year ASSESSMENT (on Performance Results achieved)',
        max_length=100,
        blank=True,
        null=True)

    kpa_rating = models.CharField(
        verbose_name='KPA RATING (Use Rating Scale)',
        max_length=5,
        choices=PERFORMANCE_RATING)

    kpa_score = models.CharField(
        verbose_name='KPA SCORE (Rating x Weighting)',
        max_length=50)

    year_end_assessment = models.CharField(
        verbose_name='Year- End or End of Contract  ASSESSMENT (on Performance'
                     ' Results achieved) Please circle relevant period',
        max_length=100,
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Key Performance Areas'
        verbose_name_plural = 'Key Performance Areas'
