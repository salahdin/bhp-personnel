from django.db import models
from django.forms import Textarea
from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .modeladmin_mixins import KPAModelAdminMixin
from ..admin_site import bhp_personnel_admin
from ..forms import StrategicOrientationForm
from ..models import StrategicOrientation


@admin.register(StrategicOrientation, site=bhp_personnel_admin)
class StrategicOrientationAdmin(KPAModelAdminMixin, admin.ModelAdmin):

    form = StrategicOrientationForm
    show_save_next = True
    show_save_prev = None
    show_cancel = True
    next_cls = 'bhp_personnel.resultsfocus'

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
        ('Strategic Orientation', {
            'fields': (
                'strategic_orientation_desc',
                'strategic_orientation',
                'strategic_orientation_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['strategic_orientation_desc', ]
