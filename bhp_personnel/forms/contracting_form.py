from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contracting


class ContractingForm(SiteModelFormMixin, forms.ModelForm):

    identifier = forms.CharField(
        label='Employee Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Contracting
        fields = '__all__'
