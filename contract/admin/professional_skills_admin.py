from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import ModelAdminNextUrlRedirectError
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import contract_admin
from ..forms import ProfessionalSkillsForm
from ..models import ProfessionalSkills


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

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


@admin.register(ProfessionalSkills, site=contract_admin)
class ProfessionalSkillsAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = ProfessionalSkillsForm

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
        ('STRATEGIC ORIENTATION', {
            'fields': (
                'strategic_orientation',
                'strategic_orientation_comm',
            )}),
        ('RESULTS FOCUS AND COMMITMENTS', {
            'fields': (
                'results_focus',
                'results_focus_comm',
            )}),
        ('TEAM LEADERSHIP AND MOTIVATION', {
            'fields': (
                'leadership_motivation',
                'leadership_motivation_comm',
            )}),
        ('INNOVATION AND CREATIVITY', {
            'fields': (
                'innovation_creativity',
                'innovation_creativity_comm',
            )}),
        ('PLANNING AND ORGANISING SKILLS', {
            'fields': (
                'planning_skills',
                'planning_skills_comm',
            )}),
        ('TEAMWORK AND INTERPERSONAL SKILLS', {
            'fields': (
                'interpersonal_skills',
                'interpersonal_skills_comm',
            )}),
        ('COMMUNICATION SKILLS', {
            'fields': (
                'communication_skills',
                'communication_skills_comm',
            )}),
        ('JOB KNOWLEDGE AND PRODUCTIVITY', {
            'fields': (
                'productivity',
                'productivity_comm',
            )}),
        ('QUALITY OF WORK', {
            'fields': (
                'quality_of_work',
                'quality_of_work_comm',
            )}),
        audit_fieldset_tuple)
