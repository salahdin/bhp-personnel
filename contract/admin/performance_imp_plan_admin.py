from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_metadata import NextFormGetter
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import TabularInlineMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import contract_admin
from ..forms import PerformanceImpPlanForm, ImprovementObjectivesForm
from ..models import PerformanceImpPlan, ImprovementObjectives


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


class ImprovementObjectivesAdmin(TabularInlineMixin, admin.TabularInline):

    model = ImprovementObjectives
    form = ImprovementObjectivesForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'effectiveness_area',
                'measures',
                'threshold_target',
                'stretch_target',
                'actual_result',
                'self_score',
                'score_by_supervisor',
                'agreed_score',
                'supervisor_comments']}
         ),)


@admin.register(PerformanceImpPlan, site=contract_admin)
class PerformanceImpPlanAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = PerformanceImpPlanForm

    inlines = [ImprovementObjectivesAdmin,]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 1,
                   'cols': 40,
                   'style': 'height: 1em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'period',
                'date',
                'appraiser',
                'employee_signature',
                'supervisor_signature',
                'employee_comments',
            )}),
        audit_fieldset_tuple)
