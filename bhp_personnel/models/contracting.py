from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract
from .job_description import JobDescription
from .list_models import Skills


class Contracting(BaseUuidModel, SiteModelMixin, models.Model):
 
 
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

    job_description = models.ForeignKey(
        JobDescription, on_delete=models.CASCADE)

    skills = models.ManyToManyField(
        Skills,
        verbose_name='Which professional skills does this personnel have? ',
        max_length=40,
        blank=True)


    other_skills = models.CharField(
        max_length=100,
        verbose_name='What other professional skills does this personnel have?',
        null=True)


    def __str__(self):
        return f'{self.job_title} Job Description'

    class Meta:
        app_label = 'bhp_personnel'
        verbose_name = 'Contracting'
        verbose_name_plural = 'Contracting'
