from django.contrib import admin

from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import ContractForm, ContractExtensionForm
from ..models import Contract, ContractExtension


class ContractExtensionAdmin(TabularInlineMixin, admin.TabularInline):
    model = ContractExtension
    form = ContractExtensionForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'ext_duration',
                'end_date')}),
        )


@admin.register(Contract, site=contract_admin)
class ContractAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContractForm
    inlines = [ContractExtensionAdmin, ]

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'job_description',
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
