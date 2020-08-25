from django.db import models

from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base

from .model_mixins import CommonDetailsMixin
from ..identifier import Identifier


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('first_name')
        fields.append('last_name')
        fields.append('email')
        fields.append('job_title')
        fields.append('employee_code')
        fields.append('identifier')
        return fields

    class Meta:
        abstract = True


class EmployeeManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, identifier):
        return self.get(
            identifier=identifier
        )


class Employee(CommonDetailsMixin, SiteModelMixin, SearchSlugModelMixin,
               models.Model):

    identifier_cls = Identifier

    identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        blank=True,
        null=True,
        unique=True)

    job_title = models.CharField(
        verbose_name="Job Title",
        max_length=150,
    )

    employee_code = models.CharField(
        verbose_name="Employee Code",
        max_length=30,
        unique=True
    )

    def natural_key(self):
        return self.identifier

    def __str__(self):
        return f'{self.first_name}, {self.last_name} {self.employee_code}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
