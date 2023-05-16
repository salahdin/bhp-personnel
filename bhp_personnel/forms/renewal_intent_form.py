from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RenewalIntent


class RenewalIntentForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contract'].disabled = True

    class Meta:
        model = RenewalIntent
        fields = '__all__'
