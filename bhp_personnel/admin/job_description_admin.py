from django.forms import Textarea
from django.db import models

from django.contrib import admin
from ..models import JobDescription, JobDescriptionKpa
from ..admin_site import bhp_personnel_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from ..forms import JobDescriptionForm, JobDescriptionKpaForm
from edc_model_admin import StackedInlineMixin


class JobDescriptionKpaInline(StackedInlineMixin, admin.StackedInline):

    model = JobDescriptionKpa
    form = JobDescriptionKpaForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }

    extra = 1
    max_num = 3
    fieldsets = (
        (None, {
            'fields': [
                'key_performance_area',
                'kpa_tasks',
                'kpa_performance_indicators',
                'skills_required',
                'kpa_grade', ]}
         ),)


@admin.register(JobDescription, site=bhp_personnel_admin)
class JobDescriptionAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = JobDescriptionForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }

    inlines = [JobDescriptionKpaInline, ]
    fieldsets = (
        (None, {
            'fields': (
                'identifier',
                'job_title',
                'supervisor',
                'job_purpose',
                'qualifications',
                'position',
                'department',
                'experience',
                'skills_and_knowledge',
            )}),
        audit_fieldset_tuple)
