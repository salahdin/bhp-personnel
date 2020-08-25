from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


class Department(BaseUuidModel, SiteModelMixin, models.Model):

    supervisor = models.CharField(
        verbose_name="Supervisor Name",
        max_length=50,
        null=False, blank=False
    )

    name = models.CharField(
        verbose_name="Department Name",
        max_length=50,
        null=False, blank=False
    )

    description = models.CharField(
        verbose_name='Description',
        max_length=200
    )

    def __str__(self):
        return f'{self.supervisor}, {self.name}'
