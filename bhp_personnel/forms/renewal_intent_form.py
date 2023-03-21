from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RenewalIntent


class RenewalIntentForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = RenewalIntent
        fields = '__all__'
