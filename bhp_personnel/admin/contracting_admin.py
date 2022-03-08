from django.forms import Textarea
from django.db import models

from django.contrib import admin
from ..models import Contracting, JobPerformanceKpa
from ..admin_site import bhp_personnel_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from ..forms import ContractingForm, JobPerformanceKpaForm
from edc_model_admin import StackedInlineMixin


class JobPerformanceKpaInline(StackedInlineMixin, admin.StackedInline):

    model = JobPerformanceKpa
    form = JobPerformanceKpaForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }

    extra = 1
    max_num = 20
    fieldsets = (
        (None, {
            'fields': [
                'key_performance_area',
                'kpa_tasks',
                'kpa_performance_indicators',
                'skills_required', ]}
         ),)


@admin.register(Contracting, site=bhp_personnel_admin)
class ContractingAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ContractingForm
    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'contract',
                'job_description',
                'skills',
            )}),
        audit_fieldset_tuple)

    inlines = [JobPerformanceKpaInline]

    filter_horizontal = ('skills', )
    list_filter = ('job_description', )
    autocomplete_fields = ['job_description', ]

    def has_change_permission(self, request, obj=None):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False

    def has_add_permission(self, request):
        if 'HR' in request.user.groups.values_list('name', flat=True):
            return True
        return False
