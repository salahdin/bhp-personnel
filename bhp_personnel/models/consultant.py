from django.db import models

from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin as Base
from edc_base.model_mixins import BaseUuidModel

from ..identifier import ConsultantIdentifier
from .employee import Employee
from .model_mixins import CommonDetailsMixin


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('first_name')
        fields.append('last_name')
        fields.append('email')
        fields.append('identifier')
        return fields

    class Meta:
        abstract = True


class Consultant(CommonDetailsMixin, SiteModelMixin, BaseUuidModel):

    identifier_cls = ConsultantIdentifier

    identifier = models.CharField(
        verbose_name="Consultant Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True)

    supervisor = models.ForeignKey(
        Employee, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name} {self.identifier}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
