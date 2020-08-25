from django.db import models

from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base

from .model_mixins import CommonDetailsMixin
from ..pi_identifier import Identifier


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


class EmployeeManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, identifier):
        return self.get(
            identifier=identifier
        )


class Consultant(CommonDetailsMixin, SiteModelMixin, models.Model):

    identifier_cls = Identifier

    identifier = models.CharField(
        verbose_name="Consultant/PI Identifier",
        max_length=36,
        blank=True,
        null=True,
        unique=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name} {self.identifier}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
