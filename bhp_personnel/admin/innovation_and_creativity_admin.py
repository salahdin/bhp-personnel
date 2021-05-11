from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import InnovationAndCreativityForm
from ..models import InnovationAndCreativity


@admin.register(InnovationAndCreativity, site=bhp_personnel_admin)
class InnovationAndCreativityAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = InnovationAndCreativityForm
    show_save_next = True
    show_save_prev = True
    show_cancel = True
    next_cls = 'bhp_personnel.planningskills'
    prev_cls = 'bhp_personnel.leadershipandmotivation'

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
        ('Innovation and Creativity', {
            'fields': (
                'innovation_creativity_desc',
                'innovation_creativity',
                'innovation_creativity_comm',
                'assessment_period_type'
            )
        }),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_period_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return ['innovation_creativity_desc', ]

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'kpa_forms': True}
        return super().extra_context(extra_context=extra_context)
