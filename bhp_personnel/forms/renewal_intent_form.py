from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RenewalIntent


class RenewalIntentForm(SiteModelFormMixin, forms.ModelForm):

    contract = forms.CharField(
        label=' Contract',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RenewalIntent
        fields = '__all__'
