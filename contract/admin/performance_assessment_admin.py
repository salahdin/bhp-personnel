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
from ..forms import PerformanceAssessmentForm
from ..forms import PerformanceAssessmentItemForm
from ..models import PerformanceAssessment
from ..models import PerformanceAssessmentItem


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


class PerformanceAssessmentItemAdmin(TabularInlineMixin, admin.TabularInline):

    model = PerformanceAssessmentItem
    form = PerformanceAssessmentItemForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'kpa_nd_objective',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


@admin.register(PerformanceAssessment, site=contract_admin)
class PerformanceAssessmentAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = PerformanceAssessmentForm

    inlines = [PerformanceAssessmentItemAdmin, ]

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
                'overall_perf_score',
                'comp_nd_pro_score',
                'final_assess_score',
                'emp_comments',
                'supervisor_comments',
                'manager',
                'manager_signature',
                'date_manager_signed',
            )}),
        ('COMPETENCIES AND PROFESSIONAL SKILLS ASSESSMENT', {
            'fields': (
                'strategic_orientation',
                'strategic_orientation_comm',
                'results_focus',
                'results_focus_comm',
                'leadership_motivation',
                'leadership_motivation_comm',
                'innovation_creativity',
                'innovation_creativity_comm',
                'planning_skills',
                'planning_skills_comm',
                'interpersonal_skills',
                'interpersonal_skills_comm',
                'communication_skills',
                'communication_skills_comm',
                'productivity',
                'productivity_comm',
                'quality_of_work',
                'quality_of_work_comm',
            )}),
        audit_fieldset_tuple)

    search_fields = ['identifier', 'employee_code', 'agreed_by',
                     'approved_by']
