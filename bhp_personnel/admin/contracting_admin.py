from django.forms import Textarea
from django.db import models

from django.contrib import admin
from ..models import Contracting, JobDescriptionKpa
from ..admin_site import bhp_personnel_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from ..forms import ContractingForm, JobDescriptionKpaForm


@admin.register(Contracting, site=bhp_personnel_admin)
class ContractingAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContractingForm
    fieldsets = (
        (None, {
            'fields': (
                'emp_identifier',
                'contract',
                'job_description',
                'skills',
                'other_skills',
            )}),
        audit_fieldset_tuple)

    filter_horizontal = ("skills",)
    list_filter = ('job_description',)

    def has_change_permission(self, request, obj=None):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False

    def has_add_permission(self, request):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False
