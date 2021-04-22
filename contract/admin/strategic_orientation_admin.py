from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.http import HttpResponseRedirect
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)

from ..admin_site import contract_admin
from ..forms import StrategicOrientationForm
from ..models import StrategicOrientation, ResultsFocus


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


@admin.register(StrategicOrientation, site=contract_admin)
class StrategicOrientationAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = StrategicOrientationForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 5,
                   'cols': 50,
                   'style': 'height: 3em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'emp_identifier',
                'contract',
            )}),
        ('Strategic Orientation', {
            'fields': (
                'strategic_orientation_desc',
                'strategic_orientation',
                'strategic_orientation_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['strategic_orientation_desc', ]

    def response_change(self, request, obj):
        if "_add_next" in request.POST:
            emp_identifier = obj.emp_identifier
            contract = obj.contract.id
            obj.save()

            try:
                next_form = ResultsFocus.objects.get(contract=contract,
                                              emp_identifier=emp_identifier)
            except ResultsFocus.DoesNotExist:
                return HttpResponseRedirect(
                    f'/admin/contract/resultsfocus/add/?,contract&contract='
                    f'{contract}&contract={contract}&emp_identifier='
                    f'{emp_identifier}')
            else:
                return HttpResponseRedirect(
                    f'/admin/contract/resultsfocus/{next_form.id}/change/?')

        return super().response_change(request, obj)
