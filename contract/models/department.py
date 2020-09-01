from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class Department(BaseUuidModel, SiteModelMixin, models.Model):

    hod = models.CharField(
        verbose_name="Head Of Department",
        max_length=50,
        null=False,
    )

    dept_name = models.CharField(
        verbose_name="Department Name",
        max_length=50,
        null=False,
    )

    description = models.CharField(
        verbose_name='Description',
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f'{self.dept_name}'
