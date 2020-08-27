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

from ..admin_site import contract_admin
from ..forms import ConsultantForm
from ..models import Consultant


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


@admin.register(Consultant, site=contract_admin)
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
                'cell',
                'email',
            )}),
        audit_fieldset_tuple)

    search_fields = ['first_name', 'last_name', 'email', 'identifier']

