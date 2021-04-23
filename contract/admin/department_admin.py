from django.contrib import admin
from edc_metadata import NextFormGetter
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import DepartmentForm
from ..models import Department


@admin.register(Department, site=contract_admin)
class DepartmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DepartmentForm
    next_form_getter_cls = NextFormGetter

    fieldsets = (
        (None, {
            'fields': (
                'hod',
                'dept_name',
                'description',
            )}),
        audit_fieldset_tuple)

    search_fields = ['supervisor', 'dept_name']
