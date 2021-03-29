from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import InnovationAndCreativityForm
from ..models import InnovationAndCreativity


@admin.register(InnovationAndCreativity, site=contract_admin)
class InnovationAndCreativityAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = InnovationAndCreativityForm

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
        ('Planning and Organising Skills', {
            'fields': (
                'innovation_creativity_desc',
                'innovation_creativity',
                'innovation_creativity_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['innovation_creativity_desc', ]
