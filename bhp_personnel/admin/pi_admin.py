from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import bhp_personnel_admin
from ..forms import PiForm
from ..models import Pi
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Pi, site=bhp_personnel_admin)
class PiAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = PiForm

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
