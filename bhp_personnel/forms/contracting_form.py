from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contracting


class ContractingForm(SiteModelFormMixin, forms.ModelForm):

    emp_identifier = forms.CharField(
        label='Employee Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    job_title = forms.CharField(
        label='Job Title',
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': 40}))

    class Meta:
        model = Contracting
        fields = '__all__'
