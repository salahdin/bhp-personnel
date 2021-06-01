from django.db import models
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin as Base
from edc_base.utils import get_utcnow


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('identifier')
        fields.append('email')
        return fields

    class Meta:
        abstract = True


class Notifications(
        SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    identifier = models.CharField(
        verbose_name="Personnel Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True)

    email = models.EmailField()

    sent_date = models.DateTimeField(default=get_utcnow)

    success_status = models.BooleanField(default=False)

    class Meta:
        app_label = "bhp_personnel"
