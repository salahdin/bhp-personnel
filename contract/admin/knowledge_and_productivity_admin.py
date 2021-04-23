from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import KPAModelAdminMixin
from ..admin_site import contract_admin
from ..forms import KnowledgeAndProductivityForm
from ..models import KnowledgeAndProductivity


@admin.register(KnowledgeAndProductivity, site=contract_admin)
class KnowledgeAndProductivityAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = KnowledgeAndProductivityForm
    show_save_next = True
    show_save_prev = True
    show_cancel = True
    next_cls = 'contract.qualityofwork'
    prev_cls = 'contract.communicationskills'

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
        ('Job Knowledge  and productivity', {
            'fields': (
                'productivity_skills_desc',
                'productivity',
                'productivity_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['productivity_skills_desc', ]
