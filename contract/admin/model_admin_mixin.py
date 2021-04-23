from django.apps import apps as django_apps
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import ModelAdminNextUrlRedirectError
from urllib.parse import urlencode


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    show_save = True
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

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'show_save': self.show_save}
        return super().extra_context(extra_context=extra_context)


class KPAModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                         ModelAdminFormInstructionsMixin,
                         ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                         ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                         ModelAdminInstitutionMixin,
                         ModelAdminRedirectOnDeleteMixin,
                         ModelAdminSiteMixin):

    def extra_context(self, extra_context=None):
        """Adds the booleans for the savenext and cancel buttons
        to the context.

        These are also referred to in the submit_line.html.
        """
        extra_context = {'kpa_forms': True,
                         'show_save_prev': True}
        return super().extra_context(extra_context=extra_context)

    def get_savenext_redirect_url(self, request=None, obj=None):
        """Returns a redirect_url for the next form in the visit schedule.

        This method expects a CRF model with model mixins from edc_visit_tracking
        and edc_visit_schedule.

        Requires edc_metadata. Queries Metadata models.
        """
        next_model_cls = django_apps.get_model(self.next_cls)

        if obj:
            contract = obj.contract.id
            emp_identifier = obj.emp_identifier

            try:
                next_model_obj = next_model_cls.objects.get(contract=contract,
                                                            emp_identifier=emp_identifier)
            except next_model_cls.DoesNotExist:

                url_name = '_'.join(
                    next_model_cls._meta.label_lower.split('.'))
                url_name = f'{self.admin_site.name}:{url_name}'
                redirect_url = reverse(f'{url_name}_add')
                opts = {'contract': contract,
                        'emp_identifier': emp_identifier}

                next_querystring = request.GET.dict().get(self.next_querystring_attr)
                querystring = urlencode(opts)
                return f'{redirect_url}?{self.next_querystring_attr}={next_querystring}&{querystring}'

            else:
                redirect_url = reverse(
                    f'{url_name}_change', args=(next_model_obj.id,))

                opts = {'contract': contract,
                        'emp_identifier': emp_identifier}

                next_querystring = request.GET.dict().get(self.next_querystring_attr)
                querystring = urlencode(opts)
                return f'{redirect_url}?{self.next_querystring_attr}={next_querystring}&{querystring}'

