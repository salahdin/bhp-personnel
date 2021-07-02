from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import LeadershipAndMotivationForm
from ..models import LeadershipAndMotivation


@admin.register(LeadershipAndMotivation, site=bhp_personnel_admin)
class LeadershipAndMotivationAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = LeadershipAndMotivationForm
    show_save_next = True
    show_save_prev = True
    show_cancel = True
    next_cls = 'bhp_personnel.innovationandcreativity'
    prev_cls = 'bhp_personnel.resultsfocus'

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
        ('Team Leadership and Motivation', {
            'fields': (
                'leadership_motivation_desc',
                'leadership_motivation',
                'leadership_motivation_comm',
                'assessment_period_type'
            )
        }),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_period_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return ['leadership_motivation_desc', ]

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'kpa_forms': True}
        return super().extra_context(extra_context=extra_context)
