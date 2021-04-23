from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import QualityOfWorkForm
from ..models import QualityOfWork


@admin.register(QualityOfWork, site=contract_admin)
class QualityOfWorkAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = QualityOfWorkForm

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
        ('Quality of Work', {
            'fields': (
                'quality_of_work_desc',
                'quality_of_work',
                'quality_of_work_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['quality_of_work_desc', ]
