from django.contrib import admin

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin, TabularInlineMixin)
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import contract_admin
from ..forms import ContractForm, ContractExtensionForm
from ..models import Contract, ContractExtension


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


class ContractExtensionAdmin(TabularInlineMixin, admin.TabularInline):
    model = ContractExtension
    form = ContractExtensionForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'ext_duration',
                'ext_end_date')}),
        )


@admin.register(Contract, site=contract_admin)
class ContractAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContractForm
    inlines = [ContractExtensionAdmin, ]

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'duration',
                'start_date',
                'end_date',
                'status')}),
        audit_fieldset_tuple
    )

    radio_fields = {
        "duration": admin.VERTICAL,
        "status": admin.VERTICAL,
    }

    list_display = [
        'created', 'duration',
        'start_date', 'end_date', 'status']

    list_filter = [
        'created', 'duration', 'start_date', 'end_date', 'status']

    search_fields = ('contract',)
