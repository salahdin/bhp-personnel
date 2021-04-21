from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .job_description import JobDescription


class JobDescriptionKpa(BaseUuidModel, SiteModelMixin, models.Model):
    job_description = models.ForeignKey(
        JobDescription,
        on_delete=models.PROTECT)
    key_performance_area = models.CharField(
        verbose_name='KEY PERFORMANCE AREAS',
        max_length=50)

    kpa_tasks = models.TextField(
        verbose_name='TASKS',
        max_length=None)

    kpa_performance_indicators = models.TextField(
        verbose_name='PERFORMANCE INDICATORS'
                     '(completion dates)',
        max_length=None, )
    skills_required = models.TextField(
        verbose_name="SKILLS REQUIRED",
        max_length=100
    )

    kpa_grade = models.CharField(
        verbose_name='Grade',
        max_length=50)

    class Meta:
        verbose_name = 'Job Description Kpa'
        verbose_name_plural = 'Job Description Kpa'
