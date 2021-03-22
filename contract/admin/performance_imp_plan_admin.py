from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import TabularInlineMixin, StackedInlineMixin, ModelAdminNextUrlRedirectError
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from ..admin_site import contract_admin
from ..forms import PerformanceImpPlanForm, ImprovementObjectivesForm
from ..models import PerformanceImpPlan, ImprovementObjectives


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


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
