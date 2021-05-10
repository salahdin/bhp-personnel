from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .department import Department
from .employee import Supervisor


class JobDescription(BaseUuidModel, SiteModelMixin, models.Model):

    identifier = models.CharField(
        verbose_name="Identifier",
        max_length=36,
        null=True,
        blank=True)

    job_title = models.CharField(
        verbose_name="Job Title",
        max_length=100)

    supervisor = models.ForeignKey(
        Supervisor, blank=False, null=False,
        on_delete=models.CASCADE)

    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    job_purpose = models.CharField(
        verbose_name="Job Purpose",
        max_length=100
    )

    qualifications = models.CharField(
        verbose_name="Qualifications",
        max_length=100)

    position = models.CharField(
        verbose_name="Position",
        max_length=100)

    experience = models.CharField(
        verbose_name="Experience",
        max_length=20)

    skills_and_knowledge = models.TextField(
        verbose_name="Skills and Knowledge",
        max_length=None)

    def __str__(self):
        return f'{self.job_title} Job Description'

    class Meta:
        app_label = 'bhp_personnel'
        verbose_name = 'Job Description'
        verbose_name_plural = 'Job Description'
