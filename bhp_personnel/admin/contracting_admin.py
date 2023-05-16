from django.forms import Textarea
from django.db import models

from django.contrib import admin
from ..models import Contracting
from ..admin_site import bhp_personnel_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from ..forms import ContractingForm


@admin.register(Contracting, site=bhp_personnel_admin)
class ContractingAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = ContractingForm
    fieldsets = (
        (None, {
            'fields': (
                'contract',
                'identifier',
                'job_description',
                'skills',
            )}),
        audit_fieldset_tuple)

    filter_horizontal = ('skills',)
    list_filter = ('job_description',)
    autocomplete_fields = ['job_description', ]

    def get_readonly_fields(self, request, obj=None):
        return ['contract', ]