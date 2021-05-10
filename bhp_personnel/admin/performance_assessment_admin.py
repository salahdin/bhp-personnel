from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import PerformanceAssessmentForm
from ..models import PerformanceAssessment


@admin.register(PerformanceAssessment, site=bhp_personnel_admin)
class PerformanceAssessmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = PerformanceAssessmentForm

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
                'review',
                'overall_perf_score',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        'review': admin.VERTICAL, }
