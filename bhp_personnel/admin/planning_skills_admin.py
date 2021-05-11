from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import PlanningSkillsForm
from ..models import PlanningSkills


@admin.register(PlanningSkills, site=bhp_personnel_admin)
class PlanningSkillsAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = PlanningSkillsForm
    show_save_next = True
    show_save_prev = True
    show_cancel = True
    next_cls = 'bhp_personnel.interpersonalskills'
    prev_cls = 'bhp_personnel.innovationandcreativity'

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
                'assessment_period_type'
            )
        }),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_period_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return ['planning_skills_desc', ]

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'kpa_forms': True}
        return super().extra_context(extra_context=extra_context)
