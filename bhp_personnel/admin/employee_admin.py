from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_metadata import NextFormGetter
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import bhp_personnel_admin
from ..forms import EmployeeForm, SupervisorForm
from ..models import Employee, Supervisor


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
    next_form_getter_cls = NextFormGetter


@admin.register(Supervisor, site=bhp_personnel_admin)
class SupervisorAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = SupervisorForm

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


@admin.register(Employee, site=bhp_personnel_admin)
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
