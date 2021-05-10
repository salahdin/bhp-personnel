from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import ModelAdminMixin

from ..admin_site import bhp_personnel_admin
from ..forms import KeyPerformanceAreaForm
from ..models import KeyPerformanceArea


@admin.register(KeyPerformanceArea, site=bhp_personnel_admin)
class KeyPerformanceAreaAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = KeyPerformanceAreaForm

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
                'kpa_nd_objective',
                'performance_indicators',
                'weighting',
                'kpa_rating',
                'kpa_score',
                'assessment_period_type')}),
        audit_fieldset_tuple)

    radio_fields = {
        'kpa_rating': admin.VERTICAL,
        'assessment_period_type': admin.VERTICAL}
