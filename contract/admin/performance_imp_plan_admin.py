from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin import StackedInlineMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import PerformanceImpPlanForm, ImprovementObjectivesForm
from ..models import PerformanceImpPlan, ImprovementObjectives


class ImprovementObjectivesAdmin(StackedInlineMixin, admin.StackedInline):

    model = ImprovementObjectives
    form = ImprovementObjectivesForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'effectiveness_area',
                'measures',
                'threshold_target',
                'stretch_target',
                'actual_result',
                'self_score',
                'score_by_supervisor',
                'agreed_score',
                'supervisor_comments']}
         ),)


@admin.register(PerformanceImpPlan, site=contract_admin)
class PerformanceImpPlanAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = PerformanceImpPlanForm

    inlines = [ImprovementObjectivesAdmin, ]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 1,
                   'cols': 40,
                   'style': 'height: 1em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'emp_identifier',
                'contract',
            )}),
        audit_fieldset_tuple)
