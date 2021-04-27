from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin import StackedInlineMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin

from ..admin_site import contract_admin
from ..forms import KeyPerformanceAreaForm
from ..models import KeyPerformanceArea


@admin.register(KeyPerformanceArea, site=contract_admin)
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
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment')}),
        audit_fieldset_tuple)

    radio_fields = {
        'kpa_rating': admin.VERTICAL}

