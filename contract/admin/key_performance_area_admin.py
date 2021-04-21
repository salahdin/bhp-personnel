from django.apps import apps as django_apps
from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.urls.base import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import StackedInlineMixin, ModelAdminNextUrlRedirectError
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin

from ..admin_site import contract_admin
from ..forms import KeyPerformanceAreaForm, KeyPerformanceAreaItemForm
from ..models import KeyPerformanceArea, KeyPerformanceAreaItem, Employee


class KeyPerformanceAreaItemAdmin(StackedInlineMixin, admin.StackedInline):

    model = KeyPerformanceAreaItem
    form = KeyPerformanceAreaItemForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'kpa_nd_objective',
                'performance_indicators',
                'weighting',
                'mid_year_performance',
                'kpa_rating',
                'kpa_score',
                'year_end_assessment']}
         ),)


@admin.register(KeyPerformanceArea, site=contract_admin)
class KeyPerformanceAreaAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = KeyPerformanceAreaForm

    inlines = [KeyPerformanceAreaItemAdmin]

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
        audit_fieldset_tuple)

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         super().save_model(request, obj, form, change)
