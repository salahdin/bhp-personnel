from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import bhp_personnel_admin
from ..forms import EmployeeForm, SupervisorForm
from ..models import Employee, Supervisor
from .modeladmin_mixins import ModelAdminMixin


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
class EmployeeAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = EmployeeForm

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'first_name',
                'middle_name',
                'last_name',
                'gender',
                'title_salutation',
                'date_of_birth',
                'highest_qualification',
                'nationality',
                'identity',
                'identity_type',
                'country',
                'postal_address',
                'physical_address',
                'department',
                'supervisor',
                'studies',
                'cell',
                'next_of_kin_contact',
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

    autocomplete_fields = ['supervisor']

    filter_horizontal = ("studies",)

    list_filter = ('department',
                   'supervisor')

    def has_change_permission(self, request, obj=None):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False

    def has_add_permission(self, request):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False
