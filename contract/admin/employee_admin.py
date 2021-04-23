from django.contrib import admin
from edc_metadata import NextFormGetter
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import EmployeeForm, SupervisorForm
from ..models import Employee, Supervisor


@admin.register(Supervisor, site=contract_admin)
class SupervisorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SupervisorForm
    next_form_getter_cls = NextFormGetter

    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'cell',
                'email',
            )}),
        audit_fieldset_tuple)

    search_fields = ['first_name', 'last_name', 'email',
                     'cell']


@admin.register(Employee, site=contract_admin)
class EmployeeAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = EmployeeForm

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'first_name',
                'middle_name',
                'last_name',
                'gender',
                'department',
                'supervisor',
                'cell',
                'email',
                'job_title',
                'hired_date',
                'employee_code',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        "gender": admin.VERTICAL,
    }

    search_fields = ['first_name', 'last_name', 'email', 'job_title',
                     'employee_code', 'identifier', 'cell']

    autocomplete_fields = ['department', 'supervisor']
