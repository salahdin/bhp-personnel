from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import KPAModelAdminMixin
from ..admin_site import contract_admin
from ..forms import InterpersonalSkillsForm
from ..models import InterpersonalSkills


@admin.register(InterpersonalSkills, site=contract_admin)
class InterpersonalSkillsAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = InterpersonalSkillsForm
    show_save_next = True
    show_cancel = True
    next_cls = 'contract.communicationskills'

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
                'interpersonal_skills_desc',
                'interpersonal_skills',
                'interpersonal_skills_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['interpersonal_skills_desc', ]

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'kpa_forms': True}
        return super().extra_context(extra_context=extra_context)
