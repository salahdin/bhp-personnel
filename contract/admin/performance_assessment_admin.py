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
from ..forms import (
    AdhereToTimeLinesForm, FollowStandardsForm, ProvideReportsForm,
    FollowTDDForm, MaintainDocumentationForm, PerformSysAnalysisForm,
    ProjectAssistanceForm, IntegrationAssistanceForm, DemonstrateInterestForm,
    ReviewTeamCodeForm, AssistResearchStaffForm, GuideJnrStaffForm,
    LeadershipSkillsForm, AssistInManagementForm, AssistInImplementationForm)
from ..models import PerformanceAssessment
from ..models import (
    AdhereToTimeLines, FollowStandards, ProvideReports, FollowTDD,
    MaintainDocumentation, PerformSysAnalysis, ProjectAssistance,
    IntegrationAssistance, DemonstrateInterest, ReviewTeamCode,
    AssistResearchStaff, GuideJnrStaff, LeadershipSkills, AssistInManagement,
    AssistInImplementation)


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


class AdhereToTimeLinesAdmin(TabularInlineMixin, admin.TabularInline):

    model = AdhereToTimeLines
    form = AdhereToTimeLinesForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'adhere_to_timelines',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class FollowStandardsAdmin(TabularInlineMixin, admin.TabularInline):

    model = FollowStandards
    form = FollowStandardsForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'follow_standards',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class ProvideReportsAdmin(TabularInlineMixin, admin.TabularInline):
    model = ProvideReports
    form = ProvideReportsForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'provide_reports',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class FollowTDDAdmin(TabularInlineMixin, admin.TabularInline):
    model = FollowTDD
    form = FollowTDDForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'follow_tdd',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class MaintainDocumentationAdmin(TabularInlineMixin, admin.TabularInline):
    model = MaintainDocumentation
    form = MaintainDocumentationForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'maintain_documentation',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class PerformSysAnalysisAdmin(TabularInlineMixin, admin.TabularInline):
    model = PerformSysAnalysis
    form = PerformSysAnalysisForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'perform_sys_analysis',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class ProjectAssistanceAdmin(TabularInlineMixin, admin.TabularInline):
    model = ProjectAssistance
    form = ProjectAssistanceForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'project_assistance',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class IntegrationAssistanceAdmin(TabularInlineMixin, admin.TabularInline):
    model = IntegrationAssistance
    form = IntegrationAssistanceForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'integration_assistance',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class DemonstrateInterestAdmin(TabularInlineMixin, admin.TabularInline):
    model = DemonstrateInterest
    form = DemonstrateInterestForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'demonstrate_interest',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class ReviewTeamCodeAdmin(TabularInlineMixin, admin.TabularInline):
    model = ReviewTeamCode
    form = ReviewTeamCodeForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'review_team_code',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class AssistResearchStaffAdmin(TabularInlineMixin, admin.TabularInline):
    model = AssistResearchStaff
    form = AssistResearchStaffForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'assist_research_staff',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class GuideJnrStaffAdmin(TabularInlineMixin, admin.TabularInline):
    model = GuideJnrStaff
    form = GuideJnrStaffForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'guide_jnr_staff',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class LeadershipSkillsAdmin(TabularInlineMixin, admin.TabularInline):
    model = LeadershipSkills
    form = LeadershipSkillsForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'leadership_skills',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class AssistInManagementAdmin(TabularInlineMixin, admin.TabularInline):
    model = AssistInManagement
    form = AssistInManagementForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'assist_in_management',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


class AssistInImplementationAdmin(TabularInlineMixin, admin.TabularInline):
    model = AssistInImplementation
    form = AssistInImplementationForm
    extra = 1
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'assist_in_implementation',
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

    inlines = [AdhereToTimeLinesAdmin, FollowStandardsAdmin,
               ProvideReportsAdmin, FollowTDDAdmin, MaintainDocumentationAdmin,
               PerformSysAnalysisAdmin, ProjectAssistanceAdmin,
               IntegrationAssistanceAdmin, DemonstrateInterestAdmin,
               ReviewTeamCodeAdmin, AssistResearchStaffAdmin,
               GuideJnrStaffAdmin, LeadershipSkillsAdmin,
               AssistInManagementAdmin, AssistInImplementationAdmin]

    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'period_covered',
                'mid_year_review',
                'year_end_review',
                'contract_end_review',
                'agreed_by',
                'supervisor_signature',
                'date_supervisor_signed',
                'employee_signature',
                'date_employee_signed',
                'approved_by',
                'signature',
                'date',
                'results_focus',
                'leadership_motivation',
                'innovation_creativity',
                'planning_skills',
                'interpersonal_skills',
                'communication_skills',
                'productivity',
                'quality_of_work',
            )}),
        audit_fieldset_tuple)

    search_fields = ['identifier', 'employee_code', 'agreed_by',
                     'approved_by']
