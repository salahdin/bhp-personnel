from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import ResultsFocusForm
from ..models import ResultsFocus


@admin.register(ResultsFocus, site=contract_admin)
class ResultsFocusAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = ResultsFocusForm

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
        ('Results Focus And Commitments', {
            'fields': (
                'results_focus_desc',
                'results_focus',
                'results_focus_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['results_focus_desc', ]
