from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import bhp_personnel_admin
from ..forms import ConsultantForm
from ..models import Consultant
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Consultant, site=bhp_personnel_admin)
class ConsultantAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = ConsultantForm

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
                'studies',
                'cell',
                'email',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        "gender": admin.VERTICAL,
    }

    search_fields = ['first_name', 'last_name', 'email', 'identifier']

    autocomplete_fields = ['supervisor']

    filter_horizontal = ("studies",)
