from django.db import models

from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import CellNumber
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin as Base

from .model_mixins import CommonDetailsMixin
from .department import Department
from .list_models import Studies
from ..identifier import EmployeeIdentifier


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


class Supervisor(BaseUuidModel):

    first_name = models.CharField(
        verbose_name="First name",
        max_length=100)

    last_name = models.CharField(
        verbose_name="Last name",
        max_length=100)

    cell = EncryptedCharField(
        verbose_name='Cell number',
        validators=[CellNumber, ],
        blank=False,)

    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        app_label = "bhp_personnel"
        unique_together = ('first_name', 'last_name', 'email')


class Employee(CommonDetailsMixin, SiteModelMixin, SearchSlugModelMixin,
               BaseUuidModel):

    identifier_cls = EmployeeIdentifier

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    studies = models.ManyToManyField(
        Studies,
        verbose_name='Which studies does this personnel belong to? ',
        max_length=20,
        blank=True)

    supervisor = models.ForeignKey(
        Supervisor, blank=False, null=False,
        on_delete=models.CASCADE)

    identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True)

    job_title = models.CharField(
        verbose_name="Job Title",
        max_length=150,)

    employee_code = models.IntegerField(
        verbose_name="Employee Code",
        unique=True)

    def natural_key(self):
        return self.identifier

    def __str__(self):
        return f'{self.first_name}, {self.last_name} {self.employee_code}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    class Meta:
        app_label = "bhp_personnel"
