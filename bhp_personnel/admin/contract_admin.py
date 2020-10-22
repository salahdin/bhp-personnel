from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from ..admin_site import bhp_personnel_admin
from ..forms import ContractForm, ContractExtensionForm
from ..models import Contract, ContractExtension
from .modeladmin_mixins import ModelAdminMixin


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


@admin.register(Contract, site=bhp_personnel_admin)
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
