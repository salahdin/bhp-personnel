from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import PlanningSkillsForm
from ..models import PlanningSkills


@admin.register(PlanningSkills, site=contract_admin)
class PlanningSkillsAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = PlanningSkillsForm

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
        ('Planning and Organising Skills', {
            'fields': (
                'planning_skills_desc',
                'planning_skills',
                'planning_skills_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['planning_skills_desc', ]
