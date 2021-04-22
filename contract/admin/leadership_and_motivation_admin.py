from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.http import HttpResponseRedirect
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import LeadershipAndMotivationForm
from ..models import LeadershipAndMotivation, InnovationAndCreativity


@admin.register(LeadershipAndMotivation, site=contract_admin)
class LeadershipAndMotivationAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = LeadershipAndMotivationForm

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
        ('Team Leadership and Motivation', {
            'fields': (
                'leadership_motivation_desc',
                'leadership_motivation',
                'leadership_motivation_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['leadership_motivation_desc', ]

    def response_change(self, request, obj):
        if "_add_next" in request.POST:
            emp_identifier = obj.emp_identifier
            contract = obj.contract.id
            obj.save()

            try:
                next_form = InnovationAndCreativity.objects.get(
                    contract=contract,
                    emp_identifier=emp_identifier)
            except InnovationAndCreativity.DoesNotExist:
                return HttpResponseRedirect(
                    f'/admin/contract/innovationandcreativity/add/?,contract&contract='
                    f'{contract}&contract={contract}&emp_identifier='
                    f'{emp_identifier}')
            else:
                return HttpResponseRedirect(
                    f'/admin/contract/innovationandcreativity/{next_form.id}/change/?')

        return super().response_change(request, obj)
