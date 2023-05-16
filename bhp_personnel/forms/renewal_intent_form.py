from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RenewalIntent


class RenewalIntentForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = RenewalIntent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RenewalIntentForm, self).__init__(*args, **kwargs)
        self.fields['contract'].disabled = True
