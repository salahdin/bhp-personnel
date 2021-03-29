from django.db import models
from django.forms import Textarea

from django.contrib import admin
from .model_admin_mixin import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import contract_admin
from ..forms import ProfessionalSkillsForm
from ..models import ProfessionalSkills


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
                'strategic_orientation_desc',
                'strategic_orientation',
                'strategic_orientation_comm',
            )
        }),
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

    def get_readonly_fields(self, request, obj=None):
        return ['strategic_orientation_desc', ]
