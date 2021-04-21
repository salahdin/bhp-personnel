from django.db import models
from django.forms import Textarea

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import ModelAdminNextUrlRedirectError

from ..admin_site import contract_admin
from ..forms import StrategicOrientationForm
from ..models import StrategicOrientation


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

    # def redirect_url(self, request, obj, post_url_continue=None):
    #     redirect_url = super().redirect_url(
    #         request, obj, post_url_continue=post_url_continue)
    #     if request.GET.dict().get('next'):
    #         # url_name = request.GET.dict().get('next').split(',')[0]
    #         url_name = '/admin/contract/strategicorientation/add/'
    #         attrs = request.GET.dict().get('next').split(',')[1:]
    #         options = {k: request.GET.dict().get(k)
    #                    for k in attrs if request.GET.dict().get(k)}
    #         try:
    #             redirect_url = url_name
    #         except NoReverseMatch as e:
    #             raise ModelAdminNextUrlRedirectError(
    #                 f'{e}. Got url_name={url_name}, kwargs={options}.')
    #     return HttpResponseRedirect(redirect_url)


@admin.register(StrategicOrientation, site=contract_admin)
class StrategicOrientationAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = StrategicOrientationForm

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

    def children_display(self, obj):
        display_text = ", ".join([
            "<a href={}>{}</a>".format(
                reverse('admin:{}_{}_change'.format(obj._meta.app_label,
                                                    obj._meta.model_name),
                        args=(strategicorientation.pk,)),
                strategicorientation.name)
            for strategicorientation in obj.strategicorientation.all()
        ])
        if display_text:
            return mark_safe(display_text)
        return "-"

    def response_change(self, request, obj):
        if "_add_next" in request.POST:
            import pdb; pdb.set_trace()
            obj.save()
            return HttpResponseRedirect("/admin/contract/resultsfocus/add/")
        return super().response_change(request, obj)
