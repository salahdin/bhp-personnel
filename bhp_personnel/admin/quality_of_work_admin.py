from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import QualityOfWorkForm
from ..models import QualityOfWork


@admin.register(QualityOfWork, site=bhp_personnel_admin)
class QualityOfWorkAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = QualityOfWorkForm
    show_save_prev = True
    show_save_next = None
    show_cancel = True
    prev_cls = 'bhp_personnel.knowledgeandproductivity'

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
                'assessment_period_type'
            )
        }),
        audit_fieldset_tuple)

    radio_fields = {
        'assessment_period_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return ['quality_of_work_desc', ]
