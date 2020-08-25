from django.contrib import admin

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import contract_admin
from ..forms import ContractForm
from ..models import Contract


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(Contract, site=contract_admin)
class ContractAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContractForm

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'duration',
                'start_date',
                'end_date',
                'active')}),
        audit_fieldset_tuple
    )

    radio_fields = {
        "duration": admin.VERTICAL,
        "active": admin.VERTICAL,
    }

    list_display = [
        'created', 'duration',
        'start_date', 'end_date', 'active']

    list_filter = [
        'created', 'duration', 'start_date', 'end_date', 'active']

    search_fields = ('temperature',)
