from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contract


class ContractForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Contract
        fields = '__all__'
