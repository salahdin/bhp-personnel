from django.contrib import admin
from edc_metadata import NextFormGetter
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import PiForm
from ..models import Pi


@admin.register(Pi, site=contract_admin)
class PiAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = PiForm
    next_form_getter_cls = NextFormGetter

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'first_name',
                'middle_name',
                'last_name',
                'gender',
                'hired_date',
                'supervisor',
                'cell',
                'email',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        "gender": admin.VERTICAL,
    }

    search_fields = ['first_name', 'last_name', 'email', 'identifier']

    autocomplete_fields = ['supervisor']
