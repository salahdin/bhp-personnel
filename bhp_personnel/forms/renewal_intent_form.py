from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RenewalIntent, Contract


class RenewalIntentForm(SiteModelFormMixin, forms.ModelForm):
    contract = forms.ModelChoiceField(label='Contract', queryset=Contract.objects.all(),
                                      widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RenewalIntent
        fields = '__all__'
