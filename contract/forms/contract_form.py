from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contract


class ContractForm(SiteModelFormMixin, forms.ModelForm):

    identifier = forms.CharField(
        label='Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Contract
        fields = '__all__'
