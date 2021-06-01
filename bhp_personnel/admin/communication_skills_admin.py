from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import CommunicationSkillsForm
from ..models import CommunicationSkills


@admin.register(CommunicationSkills, site=bhp_personnel_admin)
class CommunicationSkillsAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = CommunicationSkillsForm
    show_save_next = True
    show_save_prev = True
    show_cancel = True
    next_cls = 'bhp_personnel.knowledgeandproductivity'
    prev_cls = 'bhp_personnel.interpersonalskills'

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
        ('Communication Skills', {
            'fields': (
                'communication_skills_desc',
                'communication_skills',
                'communication_skills_comm',
                'assessment_period_type'
            )
        }),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_period_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return ['communication_skills_desc', ]
